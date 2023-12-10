from django.shortcuts import render
from .models import *


def main(request):
    return render(request, 'gov_app/vote.html')


def candidate_list(request):
    candidates = Candidate.objects.all()
    context = {
        'candidates': candidates,
    }
    return render(request, 'gov_app/candidate_list.html', context)



def party_list(request):
    parties = PoliticalParty.objects.all()
    context = {
        'parties': parties
    }
    return render(request, 'gov_app/parties_list.html', context)
