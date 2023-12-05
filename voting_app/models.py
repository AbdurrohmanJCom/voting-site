from django.db import models
from django.contrib.auth.models import User


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other voter-specific fields


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    # Add other candidate-specific fields


# gov_app/models.py
class PoliticalParty(models.Model):
    name = models.CharField(max_length=255)
    leader = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    # Add other party-specific fields
