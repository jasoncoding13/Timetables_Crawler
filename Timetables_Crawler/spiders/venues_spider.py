# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 00:26:55 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""


import os
import scrapy
from Timetables_Crawler.constants import URL_HOMEPAGE, DIR_VENUES


class VenuesSpider(scrapy.Spider):
    # Identify the spider.
    name = 'venues'
    allowed_domains = ['web.timetable.usyd.edu.au']
    custom_settings = {
            'ROBOTSTXT_OBEY': False}
    # Return an iterable of Requests (a list or write a generator function)
#    def start_requests(self):
#        urls = [
#            URL_HOMEPAGE
#            ]
#        for _u in urls:
#            yield scrapy.Request(url=_u, callback=self.parse)

    # A shortcut to the start_requests method.
    start_urls = [
            URL_HOMEPAGE
            ]

    def __init__(self, *args, **kwargs):
        if os.path.isfile(DIR_VENUES):
            self.log('Deleted file{}'.format(''))
            os.remove(DIR_VENUES)

    def parse(self, response):
        for _o in response.css('select.stdwidth#venueIdLong option'):
            yield {
                    'Venue': _o.css('::text'
                                    ).get().replace('\xa0\xa0\xa0', ' '),
                    'VenueId': _o.css('::attr("value")').get()
                    }
