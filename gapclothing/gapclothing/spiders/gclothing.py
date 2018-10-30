# -*- coding: utf-8 -*-
import scrapy


class GclothingSpider(scrapy.Spider):
	name = 'gclothing'
	allowed_domains = ['www.gap.com/browse/category.do?cid=1027221']
	start_urls = ['https://www.gap.com/browse/category.do?cid=1027221/']
	
	def parse(self, response):
		title = response.xpath('//div[@class="product-card--name"]/text()').extract()
		price = response.xpath('//div[@class="product-card-price"]/text()').extract()
		image = response.xpath('//img[@class="product-card--img"]/@src').extract()
		
		for item in zip(title,price,image):
			Details={'title' : item[0],
				'price' : item[1],
				'image' : item[2],
				}

			yield Details        
