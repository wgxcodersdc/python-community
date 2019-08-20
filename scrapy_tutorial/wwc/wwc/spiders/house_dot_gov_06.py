"""
In this example, we are filling out a form to get information from the page.
Search for a zip code, get the House representatives of that zip code.

Note that this only works for a non-javascript page. If you need a
javacript form, take a look at SplashFormRequest.

First get information about the form from Developer Tools Inspect Element
form id = header-find-rep
form element = ZIP (not in the html... but you'll see it in the network tab
"""
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
    "25322"
]


class HouseDotGovScraper(scrapy.Spider):
    """
    Scraper that submits form to house.gov to get the
    current representative for a list of zipcodes
    """
    name = 'house_dot_gov'

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
        self.log("response.url: {}".format(response.url))

        soup = BeautifulSoup(response.text, 'lxml')
        rep_divs = soup.find_all("div", {"class", "RepInfo"})
        if not rep_divs:
            rep_div = soup.find("div", id="RepInfo")
            rep_anchors = [rep_div.findChild("a")]
            rep_parties = [rep_div.findChild("p").text.strip()]
        else:
            rep_anchors = [r.findChild("a") for r in rep_divs]
            rep_parties = [r.findChild("p") for r in rep_divs]

        for a, p in zip(rep_anchors, rep_parties):
            rep_party = self._get_party(p)
            yield {
                "name": a.text.strip(),
                "website": a['href'],
                "party": rep_party
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
