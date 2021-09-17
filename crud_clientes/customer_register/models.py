from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class customer(models.Model):
    fullname = models.CharField(max_length = 100)
    emp_code = models.CharField(max_length = 3)
    mobile = models.CharField(max_length = 15)
    position = models.ForeignKey(Position, on_delete = models.CASCADE )


class City(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class requests(models.Model):
    date_hour_attention = models.DateTimeField()
    date_hour_attention_finish = models.DateTimeField()
    company = models.CharField(max_length = 150)
    city = models.ForeignKey(City, on_delete = models.CASCADE )
    affair = models.CharField(max_length = 300)
    response = models.CharField(max_length = 300)
