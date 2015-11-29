from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import PlayerProfile

class PlayerProfileCreate(CreateView):
    model = PlayerProfile
    fields = ['display_name','player_id']
    template_name = 'player/update_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerProfileCreate, self).form_valid(form)

class PlayerProfileUpdate(UpdateView):
    model = PlayerProfile
    fields = ['display_name','player_id']
    template_name = 'player/update_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerProfileUpdate, self).form_valid(form)

class PlayerProfileView(generic.DetailView):
    model = PlayerProfile
    context_object_name = 'profile'
    template_name = 'player/profile.html'

