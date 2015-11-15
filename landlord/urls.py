from django.conf.urls import patterns, url

from landlord import views

urlpatterns = patterns(
    '',
    url(r'^register/', views.register, name='landlord-register'),
)
