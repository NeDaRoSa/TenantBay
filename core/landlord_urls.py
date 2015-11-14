from django.conf.urls import patterns, url

from core import landlord

urlpatterns = patterns(
    '',
    url(r'^register/', landlord.register, name='landlord-register'),
)
