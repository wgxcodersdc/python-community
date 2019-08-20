import scrapy


class MeetupWwcSpiderFileDump(scrapy.Spider):
    """
    Scraper that fetches the start_urls and
    prints the raw response to a file called
    "wwc_spider_file_dump.html"
    """
    name = 'meetup_wwc_file_dump'

    allowed_domains = ['meetup.com']

    start_urls = ['https://www.meetup.com/Women-Who-Code-DC/']

    def parse(self, response):
        """
        This is a basic scraper.
        It's just going to print the body of the Response (its html)
        out to a file
        :param response: the html response fetched by scrapy
        :return: nothing
        """
        filename = 'wwc_spider_file_dump.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log("Saved file {}".format(filename))
