# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:22:02 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

import json as js
import os
import pandas as pd
import scrapy
from Timetables_Crawler.constants import DIR_VENUES, URL_HOMEPAGE, YEAR
from Timetables_Crawler.constants import DIR_TIMETABLES


class TimetablesSpider(scrapy.Spider):
    name = 'timetables'
    allowed_domains = ['web.timetable.usyd.edu.au']
    custom_settings = {
            'ROBOTSTXT_OBEY': False}

    try:
        with open(DIR_VENUES, 'r') as f:
            df_venues = pd.DataFrame(js.load(f), columns=['VenueId', 'Venue'])
    except FileNotFoundError as e:
        df_venues = {'VenueId': [], 'Venue': []}
        print(e)

    start_urls = [
            URL_HOMEPAGE + r'?vs=&0&mode=Bookings&rangeType=year' +
            '&uosyear=' + YEAR + '&venueId=' + str(i)
            for i in df_venues['VenueId']]

    def __init__(self, *args, **kwargs):
        if os.path.isfile(DIR_TIMETABLES):
            self.log('Deleted file{}'.format(''))
            os.remove(DIR_TIMETABLES)

    def parse(self, response):
        def _estimate_semester(dates):
            if ('Feb' in dates or
                    'Mar' in dates or 'Apr' in dates or 'May' in dates):
                return 'Semester 1'
            elif ('Aug' in dates or
                    'Sep' in dates or 'Oct' in dates or 'Nov' in dates):
                return 'Semester 2'
            else:
                return 'Out of Semesters'

        venueid = response.url.split('&')[-1].lstrip('venueId=')
        venue = self.df_venues.loc[
                self.df_venues['VenueId'] == venueid, 'Venue'].iloc[0]
        for _tr in response.css(
                'body div.section div.content table tr'):
            if _tr.css('td'):
                yield {
                        'Bookings': _tr.css(
                                'td:nth-child(1) a::text').get(),
                        'ClientOrUOS': _tr.css(
                                'td:nth-child(2) a::text').get(),
                        'Day': _tr.css('td:nth-child(3)::text').get(),
                        'Times': _tr.css('td:nth-child(4)::text').get(),
                        'Dates': _tr.css('td:nth-child(5)::text').get(),
                        'Frequency': _tr.css(
                                'td:nth-child(6)::text').get(),
                        'Capacity': _tr.css('td:nth-child(7)::text').get(),
                        'Purpose': _tr.css('td:nth-child(8)::text').get(),
                        'Venue': venue,
                        'VenueId': venueid,
                        'Semester': _estimate_semester(
                                _tr.css('td:nth-child(5)::text').get())}
            else:
                pass
