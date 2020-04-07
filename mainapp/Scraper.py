from bs4 import BeautifulSoup
import requests
from .models import Hackathons, Cities


class Webhack():
    start_url = 'https://www.hackerearth.com/hackathon/explore/city/'


    def cities(self):
        Cities.objects.all().delete()
        url = requests.get(self.start_url).text
        soup = BeautifulSoup(url, 'lxml')
        li_tag = soup.find_all('li', class_='dark large dimension inline-block')
        for li in li_tag:
            city_scraper = li.span.text
            Cities.objects.create(city=city_scraper)
            # self.webhackathons(city_scraper.lower())


    def webhackathons(self, city):
        Hackathons.objects.all().delete()
        hack = Hackathons()
        link = str(self.start_url) + str(city) + '/'
        url = requests.get(link).text
        soup = BeautifulSoup(url, 'lxml')
        tags = soup.find_all('div', class_="challenge-card-modern")
        for tag in tags:
            href = tag.a['href']
            hack_title = tag.find('div', class_='challenge-name ellipsis dark').span.text
            Hackathons.objects.create(title = hack_title,url = href)
