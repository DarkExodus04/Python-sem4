from bs4 import BeautifulSoup
import requests
from mainapp.models import Hackathons, Cities


class Webhack():
    start_url = 'https://www.hackerearth.com/hackathon/explore/city/'

    def cities(self):
        Cities.objects.all().delete()
        url = requests.get(self.start_url).text
        soup = BeautifulSoup(url, 'lxml')
        li_tag = soup.find_all('li', class_='dark large dimension inline-block')
        for li in li_tag:
            city_scraper = li.span.text
            city, created = Cities.objects.get_or_create(city = city_scraper)
            if created:
                city.save()
            # cityid = city.id
            # self.webhackathons(city_scraper,cityid)


    def webhackathons(self, city, cityid):
        city = str(city)
        city1 = city.lower().split()
        print(city, cityid)
        if len(city1) > 1:
            link = str(self.start_url) + str(city1[0]) +'-' + str(city1[1]) + '/'
        else:
            link = str(self.start_url) + str(city.lower()) + '/'
        url = requests.get(link).text
        soup = BeautifulSoup(url, 'lxml')
        tags = soup.find_all('div', class_="challenge-card-modern")
        for tag in tags:
            href = tag.a['href']
            hack_title = tag.find('div', class_='challenge-name ellipsis dark').span.text
            url = requests.get(href).text
            soup1 = BeautifulSoup(url, 'lxml')
            phase = soup1.find('div', class_='regular bold desc dark').text
            start = soup1.find('div', class_='start-time-block').text
            end = soup1.find('div', class_='end-time-block').text
            # Hackathons.objects.create(title = hack_title,url = href)
            hack, created = Hackathons.objects.update_or_create(title = hack_title, url = href, phase = phase, start = start, end = end,city_id = cityid)
            if created:
                hack.save()