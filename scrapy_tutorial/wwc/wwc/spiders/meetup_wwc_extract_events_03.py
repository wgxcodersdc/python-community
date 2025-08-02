"""
Now we want to actually extract data from our web page. But... how do we get to what we want?

A couple of options
1. Use developer tools to examine the page and get the html path
2. use scrapy shell <web_page>: https://docs.scrapy.org/en/latest/topics/shell.html
"""
from bs4 import BeautifulSoup
import scrapy


class MeetupWGXCSpiderExtractEvents(scrapy.Spider):
    """
    Scraper that fetches the start urls to get the list
    of events on the main page
    """
    name = 'meetup_WGXC_extract_events'

    allowed_domains = ['meetup.com']

    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/']

    def parse(self, response):
        """
        Extract the 'event' anchors from the meetup page
        using beautiful soup, and print them to a file
        :param response: the html response fetched by scrapy
        :return: nothing
        """
        filename = 'titles_and_links.txt'

        soup = BeautifulSoup(response.text, 'lxml')

        event_anchors = soup.findAll('a', {"class": "eventCardHead--title", "href": True})
        event_links = [a['href'] for a in event_anchors]
        event_titles = [a.text for a in event_anchors]

        with open(filename, "w") as f:
            f.write("title, link\n")
            for title, link in zip(event_titles, event_links):
                f.write("{}, {}\n".format(title, link))

        self.log("Saved file {}".format(filename))
