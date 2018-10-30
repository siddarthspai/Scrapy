# -*- coding: utf-8 -*-
import scrapy


class ClothesSpider(scrapy.Spider):
	name = 'clothes'
	allowed_domains = ['bananarepublic.gap.com/browse/category.do?cid=69883&sop=true&mlink=0000,12147468,flyout_topnav_dresses&clink=12147468']
	start_urls = ['https://bananarepublic.gap.com/browse/category.do?cid=69883&sop=true&mlink=0000,12147468,flyout_topnav_dresses&clink=12147468']

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
