# -*- coding: utf-8 -*-
import scrapy


class TinydealSpider(scrapy.Spider):
    name = 'TinyDeal'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):
        liVals = response.xpath("//ul[@class='productlisting-ul']/div[@class='p_box_wrapper']/li")
        for vals in liVals:
            title = vals.xpath(".//a/img/@title").get(),
            url = response.urljoin(vals.xpath(".//a[@class='p_box_title']/@href").get()),
            discountedPrice = vals.xpath(".//div[@class='p_box_price']/span[@class='productSpecialPrice fl']/text()").get(),
            originalPrice =   vals.xpath(".//div[@class='p_box_price']/span[@class='normalprice fl']/text()").get()

            yield{
                'titleName':title,
                'url':url,
                'discountedPrice':discountedPrice,
                'originalPrice':originalPrice
            }
        