from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/create$', views.PlayerProfileCreate.as_view(), name='profile_create'),
    url(r'^profile/update$', views.PlayerProfileUpdate.as_view(), name='profile_delete'),
    url(r'^profile/(?P<pk>[0-9]+)$', views.PlayerProfileView.as_view(), name='profile'),
]