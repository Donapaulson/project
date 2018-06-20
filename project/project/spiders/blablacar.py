# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class BlablacarSpider(scrapy.Spider):
    name = 'blablacar'
    
    def start_requests(self):
    	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    	start_url = 'https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=new+delhi&fcc=IN&tn=chandigarh&tcc=IN&sort=trip_date&order=asc&limit=10&page='
	for page in range(1,23):
		yield Request(start_url+str(page),headers=headers,callback = self.parse)
		

    def parse(self,response):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
	for i in response.xpath('//ul[@class="trip-search-results"]/li/a/@href'):
		link=response.urljoin(i.extract())
		#print link
		yield Request(link, headers=headers, callback=self.parse_this)

    def parse_this(self, response):

	source = response.xpath('//span[@class="RideName-location RideName-location--arrowAfter"]/text()').extract_first()
	#print 'source:',source
	dest = response.xpath('//span[@class="RideName-location"]/text()').extract_first()
	#print 'destination:',dest
        departure_point = response.xpath('//div[@class="RideDetails-info u-clearfix"]/span/span/text()')[0].extract()
	#print 'departure point:',departure_point.strip()
	dropoff_point = response.xpath('//div[@class="RideDetails-info u-clearfix"]/span/span/text()')[1].extract()
	#print 'dropoff point:',dropoff_point.strip()
	departure_date = response.xpath('//strong[@class="RideDetails-infoValue"]/span/text()').extract_first()
	#print 'departure date:',departure_date.strip()
	options = response.xpath('//span[@class="u-alignMiddle"]/text()').extract_first()
	#print 'options:',options
	price = response.xpath('//span[@class="Booking-price u-block"]/text()').extract_first()
	#print 'price:',price
	seats_left = response.xpath('//span[@class="Booking-seats u-block"]/b/text()').extract_first()
	#print 'seats left:',seats_left
	car_owner_image = response.xpath('//a[@class="PhotoWrapper PhotoWrapper--medium"]/img/@src').extract_first()
	#print 'carowner image:',car_owner_image
	car_owner_name = response.xpath('//div[@class="ProfileCard-infosBlock"]/h4/a/text()').extract_first()
	#print 'carowner name:',car_owner_name
	car_owner_age = response.xpath('//div[@class="ProfileCard-info"]/text()').re(r'(\d)')
	car_owner_age = ''.join(car_owner_age)
	#print 'carowner age:',''.join(car_owner_age)
	car_owner_rating = response.xpath('//span[@class="u-textBold u-darkGray"]/text()').extract_first()
	if car_owner_rating != None:
		car_owner_rating = car_owner_rating.split('/')
		car_owner_rating = car_owner_rating[0]
		#print 'car_owner_rating:',car_owner_rating
	car_model = None
	car_color = None
	car = response.xpath('//p[@class="Profile-carDetails u-cell"]/text()').extract()
	if car != []:
		car_model = car[0]
		car_color = car[1]
		car_color = car_color.split(':')
		car_color = car_color[1]
		#print 'car_model:',car_model
		#print 'car_color:',car_color
	

	data = {
		   	"Source":source,
		   	"Destination":dest,
	           	"Departure_point":departure_point,
	           	"Dropoff_point" :dropoff_point,
	           	"Departure_date" :departure_date,
			"Schedule_flexibility" :'',
			"Detour" :'',
			"Luggage_size" :'',
	           	"Options" :options,
	           	"Price" :price,
	           	"Seats_left" :seats_left,
	           	"car_owner_image " :car_owner_image,
			"Car_owner_name" :car_owner_name,
	         	"Car_owner_age" :car_owner_age,
	          	"Car_owner_experience" :'',
	           	"Car_owner_rating" :car_owner_rating,
			"Car_model" :car_model,
			"Car_rating" :'',
	           	"Car_color" :car_color
	    	}
	yield data
	





