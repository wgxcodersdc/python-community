"""
Now we are going to use a Scrapy Item and build a simple Pipeline
to do some pre-processing on our data

This file depends on items.py and pipelines.py.

"""
import datetime
import urllib.parse as urlparse

from bs4 import BeautifulSoup
import scrapy

zips = [
    "22301",
    "20009",
    "21201",
    "22312",
    "22555",
    "22603",
    "22611",
    "24608",
    "25322",
    # oops! we have a duplicate here!
    "24608",
]


class HouseDotGovPipelineScraper(scrapy.Spider):
    """
    Scraper that submits form to house.gov to get the
    current representative for a list of zipcodes

    This scraper passes its items through two pipelines for cleanup
    """
    name = 'house_dot_gov_pipeline'

    # we ONLY want our pipeline for HouseDotGov,
    # so we define it like this instead of in settings.py
    custom_settings = {
        'ITEM_PIPELINES': {
            'WGXC.pipelines.HouseDotGovDupesPipeline': 100,
            'WGXC.pipelines.HouseDotGovDemsOnlyPipeline': 500,
        }
    }

    start_urls = ['https://www.house.gov/']

    def _get_party(self, party_string):
        """
        Return the party abbreviation based on
        the contents of the party string
        """
        if "Democrat" in party_string:
            return "D"
        if "Republican" in party_string:
            return "R"
        if "Independent" in party_string:
            return "I"
        return "O"

    def parse_detail_page(self, response):
        """
        Get the representative(s) name, website, and party
        """
        parsed = urlparse.urlparse(response.url)
        zipcode = urlparse.parse_qs(parsed.query)['ZIP'][0]

        now = datetime.datetime.now(datetime.timezone.utc)

        self.log("response.url: {}".format(response.url))

        soup = BeautifulSoup(response.text, 'lxml')
        rep_divs = soup.find_all("div", {"class", "RepInfo"})
        if not rep_divs:
            rep_div = soup.find("div", id="RepInfo")
            rep_anchors = [rep_div.findChild("a")]
            rep_parties = [rep_div.findChild("p").text]
        else:
            rep_anchors = [r.findChild("a") for r in rep_divs]
            rep_parties = [r.findChild("p").text for r in rep_divs]

        for a, p in zip(rep_anchors, rep_parties):
            rep_party = self._get_party(p)
            yield {
                "name": a.text.strip(),
                "website": a['href'],
                "party": rep_party,
                "scrape_date": now,
                "zip": zipcode
            }

    def parse(self, response):
        """
        Start on the main house page, then fill out
        the form for each zipcode and get the representative info
        """
        for zipcode in zips:
            yield scrapy.FormRequest.from_response(
                response,
                formid="header-find-rep",
                formdata={"ZIP": zipcode},
                callback=self.parse_detail_page
            )
