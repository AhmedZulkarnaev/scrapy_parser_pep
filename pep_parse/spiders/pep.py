import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('a::attr(href)').re(r'pep-\d{4}/')
        for pep in peps:
            yield response.follow(pep, self.parse_pep)

    def parse_pep(self, response):
        number = response.css('h1.page-title::text').re_first(r'PEP (\d+)')
        name = response.css('h1.page-title::text').get()
        status = response.xpath(
            '//dt[contains(text(), "Status")]/following-sibling::dd[1]/text()'
        ).get()

        yield PepParseItem(
            name=name,
            number=number,
            status=status,
        )
