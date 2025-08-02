"""
This is an empty Scrapy Spider created using genspider

You likely need to clean up allowed_domains and start_urls

At a minimum a spider needs the following:
1. a name: Used when you call scrapy crawl <spider>. Must be unique.
2. start_urls: tells Scrapy where to start
3. parse method: tells Scrapy what to do

"""
import scrapy


class MeetupWGXCSpiderEmpty(scrapy.Spider):
    """
    The most basic scraper. It will fetch the
    start_url, but won't do anything with the response.
    """

    # Unique name for using the spider on the command line
    name = 'meetup_WGXC_empty'

    # domains that the spider is allowed to visit
    allowed_domains = ['meetup.com']

    # the list of urls where the spider will start from
    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/']

    # the default callback used by scrapy to process the responses it downloads
    # this is where we can add BeautifulSoup to parse html

    # the parse method usually does the following:
    # 1. parses the response,
    # 2. extracts the scraped data into dictionaries,
    # 3. and also finds new urls to follow/creates new requests
    def parse(self, response):
        """
        This parse method doesn't do anything with the response
        :param response: the html response fetched by scrapy
        :return: nothing
        """
        self.log("called parse")
