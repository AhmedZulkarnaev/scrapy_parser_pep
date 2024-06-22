import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import domain


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [domain]
    start_urls = ['https://' + domain + '/']

    def parse(self, response):
        peps = response.css('a::attr(href)').re(r'pep-\d{4}/')
        for pep in peps:
            yield response.follow(pep, self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().split(' – ', 1)
        )
        status = response.css('abbr::text').get()
        yield PepParseItem(
            name=name,
            number=number,
            status=status,
        )
