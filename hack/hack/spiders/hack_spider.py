import scrapy
from ..items import HackItem
from mainapp.models import Hackathons

class Hack_Spider(scrapy.Spider):
    name = "hack_spider"
    start_urls = ["https://www.hackerearth.com/hackathon/explore/city/mumbai/"]
    def parse(self, response):
        Hackathons.objects.all().delete()
        item = HackItem()
        all_hacks = response.css("div.challenge-card-modern")
        for hack in all_hacks:
            item['title'] = hack.css(".align-center .challenge-list-title::text").extract()
            item['url'] = hack.css("div.challenge-card-modern a::attr(href)").extract()
            yield item