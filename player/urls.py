from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/update$', views.PlayerProfileUpdate.as_view(), name='profile_update'),
    url(r'^profile/(?P<pk>[0-9]+)$', views.PlayerProfileView.as_view(), name='profile'),
    url(r'^profile/$', views.MyProfileView.as_view(), name='my_profile'),
]