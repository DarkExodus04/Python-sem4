# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from mainapp.models import Hackathons,Cities

class HackPipeline(object):

    def process_item(self, item, spider):
        hackathons = Hackathons()
        filteredtitle = ''.join((filter(lambda x: x not in ['[', ']'], item["title"])))
        hackathons.title = filteredtitle
        filteredurl = ''.join((filter(lambda x: x not in ['[', ']'], item["url"])))
        hackathons.url = filteredurl
        hackathons.save()
        # city = Cities()
        # filteredcity = ''.join((filter(lambda x: x not in ['[', ']'], item["city"])))
        # city.city =filteredcity
        # city.save()
        return item
