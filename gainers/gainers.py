import scrapy
import urllib.parse
import time

from dataTransformer import DataTransformer
from kafkaPublisher import KafkaPublisher
from configMaster import ConfigMaster

class GainersSpider(scrapy.Spider):
	configMaster = ConfigMaster()
	name = configMaster.config["spider_name"]
	start_urls = configMaster.config["start_urls"]
	delay_time = configMaster.config["delay_time"]
	headers = configMaster.config["headers"]
	timespans = configMaster.config["timespans"]

	data_transformer = DataTransformer()
	kafka_publisher = KafkaPublisher()
	markets_cache = set()

	def parse(self, response):
		for header in self.headers:
			body = response.css('.tab-content div[id*="'+header+'"]')
			for timespan in self.timespans:
				for coin in body.css('tr[id*="'+timespan+'"]'):
					link_data = {
						'timespan': self.get_timespan(header, timespan),
						'link': coin.css('.link-secondary::attr(href)').extract_first(),
						'name': coin.css('.link-secondary::text').extract_first(),
						'acronym': coin.css('.text-left::text').extract_first(),
						'volume': coin.css('.volume::text').extract_first(),
						'price': coin.css('.price::text').extract_first(),
						'change': coin.css('[class*="percent"]::text').extract_first()
					}
					self.save_data(link_data, "coin")
					next_page = self.get_next_page(response, link_data)
					self.delay()

					if next_page is not None:
						yield response.follow(next_page, self.parse_specific)

	def parse_specific(self, response):
		for market in response.css('#markets-table > tbody > tr'):
			market_data = {
				'name': market.css('.link-secondary::text').extract_first(),
				'acronym': market.css('td:nth-child(3) > a::text').extract_first(),
				'volume': market.css('td:nth-child(4) > span::text').extract_first(),
				'price': market.css('td:nth-child(5) > span::text').extract_first(),
				'volume %': market.css('td:nth-child(6) > span::text').extract_first(),
				'category': market.css('td:nth-child(7)::text').extract_first(),
				'fee type': market.css('td:nth-child(8)::text').extract_first(),
				'updated': market.css('td:nth-child(9)::text').extract_first(),
			}
			self.save_data(market_data, "market")

	def save_data(self, data, data_type):
		transformed_data = self.data_transformer.transform(data, data_type)
		self.kafka_publisher.publish(transformed_data)

	def get_timespan(self, header, timespan):
		return header + "-" + timespan

	def get_next_page(self, response, link_data):
		next_page = response.urljoin(link_data['link'])
		next_page += "#markets"
		if self.is_market_cached(next_page):
			return None
		self.add_to_markets_cache(next_page)
		return next_page

	def is_market_cached(self, next_page):
		return next_page in self.markets_cache

	def add_to_markets_cache(self, next_page):
		self.markets_cache.add(next_page)

	def delay(self):
		time.sleep(self.delay_time)
