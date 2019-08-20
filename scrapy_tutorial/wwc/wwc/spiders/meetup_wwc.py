"""


"""
import scrapy


class MeetupWwcSpider(scrapy.Spider):
    """
    Scraper to fetch the Upcoming Events from the start url
    and save the data to a file
    """
    name = 'meetup_wwc'

    allowed_domains = ['meetup.com']

    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/']

    def parse(self, response):
        """
        This is an empty scraper. It isn't going to do anything with the information it fetches.
        :param response: Scrapy response object
        :return:
        """
        pass


# TODO: we want to fetch the list of events out of this scraper
