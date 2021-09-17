from django.db import models
from datetime import datetime, date

# Create your models here.

class City(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Requests(models.Model):
    date_hour_attention = models.DateTimeField(auto_now_add = False, auto_now = False, blank = True)
    date_hour_attention_finish = models.DateTimeField(auto_now_add = False, auto_now = False, blank = True)
    date_request =  models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    company = models.CharField(max_length = 150)
    city = models.ForeignKey(City, on_delete = models.CASCADE )
    affair = models.CharField(max_length = 300)
    response = models.CharField(max_length = 300)
