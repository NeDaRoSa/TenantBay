from django.conf.urls import patterns, url

from tenant import views

urlpatterns = patterns(
    '',
    url(r'^register/', views.register, name='tenant-register'),
)

