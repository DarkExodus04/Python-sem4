import scrapy
from .. items import CityItem
from mainapp.models import Cities


class City_Spider(scrapy.Spider):
    name = "city"
    start_urls = ["https://www.hackerearth.com/hackathon/explore/city/"]

    def parse(self, response):
        Cities.objects.all().delete()
        item = CityItem()
        for i in range(43):
            item['city'] = response.css(".medium-margin-left::text")[i].extract()
            yield item