from django.urls import path
from . import views

urlpatterns = [
    path('candidate_list/', views.candidate_list, name='candidate_list'),
    path('party_list/', views.party_list, name='party_list'),
]
