"""
Some websites are too javascript-heavy to work like the
previous example. These pages are loading via
javascript, after the request is made by scrapy.

You'll know because you'll start getting
nothing or unexpected results for response.text

This example logs an error about NoneType, and
doesn't return anything.

To see what scrapy is getting back when it calls the url:
    scrapy fetch --nolog https://example.com > response.html

"""
from bs4 import BeautifulSoup
import scrapy


class MeetupWwcSpiderAttendeesBroken(scrapy.Spider):
    """
    Scraper that scrapes for all the attendees at a meetup
    """
    zips = ["22301", "20009", "21201"]

    name = 'meetup_attendees_broken'

    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/events/263644426/attendees/']

    def parse(self, response):
        """
        Get the list of attendees on the AttendeeList page for this event
        """
        self.log("response.url: {}".format(response.url))

        soup = BeautifulSoup(response.text, 'lxml')

        ul = soup.find("ul", {"class": "attendees-list"})
        attendee_links = ul.findChildren("a")

        for a in attendee_links:
            yield {"attendee_url": a}
