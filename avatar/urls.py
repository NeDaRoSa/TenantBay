from django.conf.urls import patterns, url
from avatar import views

urlpatterns = patterns(
    '',
    url(r'^upload/', views.upload_picture, name='avatar-upload'),
)
