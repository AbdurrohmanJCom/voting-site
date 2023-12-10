from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    # Add other voting_app URLs
]
