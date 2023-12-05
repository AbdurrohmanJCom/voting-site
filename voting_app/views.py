from django.shortcuts import render
from .models import User


def vote(request):
    voters = User.objects.all()
    return render(request, 'voting_app/vote.html', {'voters': voters})
