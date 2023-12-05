from django.urls import path
from .views import vote

urlpatterns = [
    path('vote/', vote, name='vote'),
    # Add other voting_app URLs
]
