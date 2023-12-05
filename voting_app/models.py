from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=15)
    thirdname = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField()                                   
    date_created = models.DateTimeField(auto_now_add=True)
    identification = models.PositiveIntegerField()

