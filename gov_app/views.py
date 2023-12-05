from django.shortcuts import render
from .models import User


def main(request):
    return render(request, 'gov_app/vote.html')
