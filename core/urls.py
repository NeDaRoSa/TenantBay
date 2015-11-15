from django.conf.urls import patterns, url
import core.views

urlpatterns = patterns(
    '',
    url(r'^login/', core.views.user_login, name='login'),
    url(r'^logout/', core.views.user_logout, name='logout'),
)
