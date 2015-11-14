from django.conf.urls import patterns, url

from core import tenant

urlpatterns = patterns(
    '',
    url(r'^register/', tenant.register, name='tenant-register'),
)

