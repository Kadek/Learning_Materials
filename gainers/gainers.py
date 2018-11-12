import scrapy
import urllib.parse

class GainersSpider(scrapy.Spider):
    name = "gainers"
    start_urls = [
        'https://coinmarketcap.com/gainers-losers/',
    ]

    def parse(self, response):
        #for coin in response.css('tr[id*="7d"]'):
        coin = response.css('tr[id*="7d"]')[0]
        link_data = {
            'link': coin.css('.link-secondary::attr(href)').extract_first(),
            'name': coin.css('.link-secondary::text').extract_first(),
            'acronym': coin.css('.text-left::text').extract_first(),
            'volume': coin.css('.volume::text').extract_first(),
            'price': coin.css('.price::text').extract_first(),
            'change': coin.css('.percent-7d::text').extract_first()
        }

        next_page = response.urljoin(link_data['link'])
        next_page += "#markets"
        if next_page is not None:
            yield response.follow(next_page, self.parse_specific)

    def parse_specific(self, response):
        for market in response.css('#markets-table > tbody > tr'):
            yield {
                'name': market.css('.link-secondary::text').extract_first(),
                'acronym': market.css('td:nth-child(3) > a::text').extract_first(),
                'volume': market.css('td:nth-child(4) > span::text').extract_first(),
                'price': market.css('td:nth-child(5) > span::text').extract_first(),
                'volume %': market.css('td:nth-child(6) > span::text').extract_first(),
                'category': market.css('td:nth-child(7)::text').extract_first(),
                'fee type': market.css('td:nth-child(8)::text').extract_first(),
                'updated': market.css('td:nth-child(9)::text').extract_first(),
            } 
    