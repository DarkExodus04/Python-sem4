from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.city

class Hackathons(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + str(self.url)

