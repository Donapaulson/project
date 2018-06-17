# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'

    def start_requests(self):
        url = 'https://www.blablacar.in/trip-delhi-chandigarh-1133453960'

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
	yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):

	source = response.xpath('//span[@class="RideName-location RideName-location--arrowAfter"]/text()').extract_first()
	print 'source:',source
	dest = response.xpath('//span[@class="RideName-location"]/text()').extract_first()
	print 'destination:',dest
        
