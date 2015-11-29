from django.shortcuts import render

from django.conf import settings
from django.views import generic

from .models import Match

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'match/index.html'
    context_object_name = 'latest_matches_list'

    def get_queryset(self):
        """Return the last five published matches."""
        return Match.objects.order_by('-timestamp_created')[:5]

