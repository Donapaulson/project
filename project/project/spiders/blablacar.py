# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'

    def start_requests(self):
        url = 'https://www.blablacar.in/trip-delhi-chandigarh-1133453960'
	#url = 'https://www.blablacar.in/trip-new-delhi-chandigarh-1134196478'
	#url = 'https://www.blablacar.in/trip-delhi-chandigarh-1134442528'

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
	yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):

	source = response.xpath('//span[@class="RideName-location RideName-location--arrowAfter"]/text()').extract_first()
	print 'source:',source
	dest = response.xpath('//span[@class="RideName-location"]/text()').extract_first()
	print 'destination:',dest
        departure_point = response.xpath('//div[@class="RideDetails-info u-clearfix"]/span/span/text()')[0].extract()
	print 'departure point:',departure_point.strip()
	dropoff_point = response.xpath('//div[@class="RideDetails-info u-clearfix"]/span/span/text()')[1].extract()
	print 'dropoff point:',dropoff_point.strip()
	departure_date = response.xpath('//strong[@class="RideDetails-infoValue"]/span/text()').extract_first()
	print 'departure date:',departure_date.strip()
	options = response.xpath('//span[@class="u-alignMiddle"]/text()').extract_first()
	print 'options:',options
	price = response.xpath('//span[@class="Booking-price u-block"]/text()').extract_first()
	print 'price:',price
	seats_left = response.xpath('//span[@class="Booking-seats u-block"]/b/text()').extract_first()
	print 'seats left:',seats_left
	car_owner_image = response.xpath('//a[@class="PhotoWrapper PhotoWrapper--medium"]/img/@src').extract_first()
	print 'carowner image:',car_owner_image
	car_owner_name = response.xpath('//div[@class="ProfileCard-infosBlock"]/h4/a/text()').extract_first()
	print 'carowner name:',car_owner_name
	car_owner_age = response.xpath('//div[@class="ProfileCard-info"]/text()').re(r'(\d)')
	print 'carowner age:',''.join(car_owner_age)
	car_owner_rating = response.xpath('//span[@class="u-textBold u-darkGray"]/text()').extract_first()
	if car_owner_rating != None:
		car_owner_rating = car_owner_rating.split('/')
		print 'car_owner_rating:',car_owner_rating[0]
	car_model = response.xpath('//p[@class="Profile-carDetails u-cell"]/text()').extract_first()
	print 'car_model:',car_model
	car_color = response.xpath('//p[@class="Profile-carDetails u-cell"]/text()')[1].extract()
	#print 'car_color:',car_color
	if car_color != None:
		car_color = car_color.split(':')
		print 'car_color:',car_color[1].strip()

