from django.urls import path
from .views import *

urlpatterns = [
    path('candidate_list/', candidate_list, name='candidate_list'),
    path('party_list/', party_list, name='party_list'),
]
