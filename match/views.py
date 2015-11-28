from django.shortcuts import render

from django.conf import settings
from django.views.generic.base import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'match/index.html'

index = Index.as_view()
