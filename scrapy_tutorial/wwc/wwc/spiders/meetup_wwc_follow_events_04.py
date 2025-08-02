"""
Let's scrape the page again, but now we will 'yield' the urls for each event,
then Scrapy will visit each of them and do some additional processing.

Do the following:
1. get the title and date data for each event
2. follow the link for each event to get some more information
3. run this spider like so to get an output file in json:

    scrapy crawl meetup_WGXC_follow_events -o event_data.json

If we want to use scrapy shell to explore a response:

    scrapy shell https://www.meetup.com/Women-Who-Code-DC/

>> from bs4 import BeautifulSoup
>> event_anchors = soup.findAll('a', {"class": "eventCardHead--title", "href": True})
>> print(event_anchors)

"""
import dateutil.parser as date_parser
from bs4 import BeautifulSoup
import scrapy


class MeetupWGXCSpiderFollowEvents(scrapy.Spider):
    """
    Scraper that fetches the start urls to get the list
    of events on the main page, then follows the event
    urls to get more information about each event
    """
    name = 'meetup_WGXC_follow_events'

    allowed_domains = ['meetup.com']

    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/']

    def parse_event_page(self, response):
        """
        This method parses the html returned by an Event detail page

        Will fetch the following:
            Date:
            Title:
            Is_waitlisted

        :param response: Scrapy Response object
        """
        self.log("response.url: {}".format(response.url))
        soup = BeautifulSoup(response.text, 'lxml')

        # title
        event_title = soup.find("h1", {"class": "pageHead-headline text--pageTitle"}).text

        # date in ISO format
        event_date = soup.find("span", {"class": "eventTimeDisplay-startDate"}).find("span").text
        event_time = soup.find("span", {"class": "eventTimeDisplay-startDate-time"}).find("span").text
        event_datetime = date_parser.parse("{} {}".format(event_date, event_time))
        event_date_iso = event_datetime.isoformat()

        # is this event waitlisted?
        event_status = soup.find("p", {"class": "eventStatusIndicator-status"}).find("span").text
        event_waitlisted = True if "join waitlist" in event_status.lower() else False

        yield {
            "event_title": event_title,
            "event_date": event_date_iso,
            "is_waitlisted": event_waitlisted
        }

    def parse(self, response):
        """
        Extract the 'event' anchors from the meetup page
        using beautiful soup, and print them to a file
        :param response: the html response fetched by scrapy
        """
        soup = BeautifulSoup(response.text, 'lxml')
        event_anchors = soup.findAll('a', {"class": "eventCardHead--title", "href": True})
        event_links = [a['href'] for a in event_anchors]

        # now we want to follow the links we found, and handle them with another method
        for link in event_links:
            # Response object has a 'follow' method for going to the next relative url
            yield response.follow(link, callback=self.parse_event_page)
