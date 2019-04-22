# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
import time


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3/']

    off=0

    def parse(self, response):
        movies=response.css('.movie-item-title')
        for movie in movies:
            #item=MaoyanItem()
            url=movie.css('a::attr(href)').extract_first()
            url='https://maoyan.com'+url
            #item['name']=movie.css('a::text').extract_first()
            item=scrapy.Request(url=url,callback=self.parse_item)
            yield item
        
        if self.off<50000:
            self.off+=30

        time.sleep(0.5)
        #url=response.xpath('//ul[@class="list-pager"]//a[contains(.,"下一页")]/@href').extract_first()
        #url='https://maoyan.com'+url
        url='https://maoyan.com/films?showType=3&offset='+str(self.off)
        yield scrapy.Request(url=url,callback=self.parse)

    def parse_item(self, response):
        item=MaoyanItem()
        item['name']=response.css('.banner .name::text').extract_first()
        item['ename']=response.css('.banner .ename::text').extract_first()
        item['director']=response.css('.celebrity .name::text').extract_first().strip()
        more=response.css('.banner .ellipsis::text').extract()
        item['movietype']=more[1].strip()
        k=more[2].find('\n',1)
        item['location']=more[2][0:k].strip()
        item['movietime']=more[2][k+3:].strip()
        item['maidenshow']=more[3].strip()
        #item['more']=more
        item['content']=response.css('.mod-content .dra::text').extract_first()
        return item

