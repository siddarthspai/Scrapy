# -*- coding: utf-8 -*-
import scrapy


class ClothingSpider(scrapy.Spider):
	name = 'rclothing'
	allowed_domains = ['www.ralphlauren.com/men-clothing-dress-shirts']
	start_urls = ['https://www.ralphlauren.com/men-clothing-dress-shirts']

	def parse(self, response):
		title=response.xpath('//a[@class="name-link"]/text()').extract()
		price=response.xpath('//span[@class="product-sales-price"]/text()').extract()
		image= response.xpath('//img[@class="default-img"]/@src').extract()
	
		for item in zip(title,price,image):
			Details={'title' : item[0],
				'price' : item[1],
				'image' : item[2],
				}
			yield Details
