from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=15)
    thirdname = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField()                                   
    date_created = models.DateTimeField(auto_now_add=True)
    series_passport = models.CharField(max_length=2)
    identification = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.firstname} {self.secondname}'


class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voted_candidate = models.IntegerField()
    voted_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.firstname} {self.user.secondname} {self.voted_candidate}'

