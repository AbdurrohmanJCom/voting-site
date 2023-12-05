from django.shortcuts import render
from .models import Voter


def vote(request):
    voters = Voter.objects.all()
    return render(request, 'voting_app/vote.html', {'voters': voters})
