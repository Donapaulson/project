# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class TestSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['blablacar.in']
    #start_url = ['https://www.blablacar.in/trip-delhi-chandigarh-1131918825']

    def parse(self, response):
	url = 'https://www.blablacar.in/trip-delhi-chandigarh-1131918825'

	h = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','accept-encoding': 'gzip,deflate, br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','referer': 'https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}


 	r = Request(url,headers=h)

 	fetch(r)
	print(response.text)


