from django.db import models
from voting_app.models import User


class PoliticalParty(models.Model):
    title = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='', null=True, blank=True)
    leader = models.OneToOneField('gov_app.Candidate', on_delete=models.SET_NULL, null=True, blank=True)
    ideology = models.TextField()
    year_founded = models.DateField()
    slogan = models.CharField(max_length=255)
    social_media_links = models.URLField(max_length=255, blank=True, null=True)
    contact_information = models.TextField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='', null=True, blank=True)
    party = models.ForeignKey(PoliticalParty, on_delete=models.SET_NULL, null=True, blank=True)
    biography = models.TextField()
    contact_information = models.TextField()
    social_media_links = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.user.firstname} {self.user.secondname} | {self.social_media_links}'