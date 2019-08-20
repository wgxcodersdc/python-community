"""
There are some workarounds for javascript-heavy pages:

1. Try to find the urls that the javascript calls use (eg, api.your.site)
2. Use selenium or splash to help render javascript

*** Note: This example requires Splash ***

We are not installing Splash as part of this lab. This one is just to demo,
and it requires docker and splash:

    docker run -p 8050:8050 scrapinghub/splash

But you if you want to later, you can go to:
https://github.com/scrapy-plugins/scrapy-splash
https://splash.readthedocs.io/en/stable/

"""
from bs4 import BeautifulSoup
import scrapy
import scrapy_splash


# copy-paste this script from the splash website
# you shouldn't have to use the lua script in the Request,
# but i can't get it to work otherwise...
lua_script = """function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(3))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end"""


class MeetupWwcSpiderAttendeesSplash(scrapy.Spider):
    """
    Scraper that scrapes for all the attendees at a meetup

    """
    zips = ["22301", "20009", "21201"]

    name = 'meetup_attendees_splash'

    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/events/263644426/attendees/']

    def start_requests(self):
        """
        Handle start_requests directly so we can explicitly return
        SplashRequest objects with a three second wait.
        """
        for url in self.start_urls:
            yield scrapy_splash.SplashRequest(
                url,
                self.parse,
                endpoint="execute",
                args={"lua_source": lua_script}
                )

    def parse(self, response):
        """
        Get the list of attendees on the AttendeeList page for this event
        """
        self.log("response.url: {}".format(response.url))

        soup = BeautifulSoup(response.text, 'lxml')
        ul = soup.find("ul", {"class": "attendees-list"})
        member_divs = ul.findAll("div", {"class": "member-item"})
        attendee_anchors = [member_div.findChild("a")
                            for member_div in member_divs]
        for a in attendee_anchors:
            href = a['href']
            name = a.text
            yield {
                "url_fragment": href,
                "name": name
            }
