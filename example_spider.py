# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:20:50 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

import os
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = [
            'https://web.timetable.usyd.edu.au/menu.jsp?siteMap=true'
            ]

    def __init__(self):
        # Count the number of pages crawled.
        self.num = 0
        # Regenerate the file items.json.
        if os.path.isfile('./items.json'):
            os.remove('./items.json')

    def parse(self, response):
        for a in response.css('li.siteMapItem a'):
            yield {
                    (str(self.num)): a.css('::text').get(),
                    }
        self.num += 1

        # Note that the next page is the same as the initial page.
        # Demonstrate it can follow the link to the next page.
        # Actually crawl the initial page twice.
        next_page = response.css('td.footer a::attr("href")').get()
        if next_page is not None and self.num < 2:
            yield response.follow(next_page, self.parse)
