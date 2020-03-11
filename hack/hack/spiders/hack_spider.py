import scrapy
from ..items import HackItem
from mainapp.models import Hackathons
from scrapy.crawler import CrawlerProcess

class Hack_Spider(scrapy.Spider):
    name = "hack_spider"

    def __init__(self,key):
        self.key = key
        url = "https://www.hackerearth.com/hackathon/explore/city/"+ key +"/"
        self.start_urls = [url]

    def parse(self, response):
        Hackathons.objects.all().delete()
        item = HackItem()
        all_hacks = response.css("div.challenge-card-modern")
        for hack in all_hacks:
            item['title'] = hack.css(".align-center .challenge-list-title::text").extract_first()
            item['url'] = hack.css("div.challenge-card-modern a::attr(href)").extract_first()
            yield item