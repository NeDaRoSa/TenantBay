from django.conf.urls import patterns, url, include

from tenant import views

urlpatterns = patterns(
    '',
    url(r'^register/', views.register, name='tenant-register'),
    url(r'^home/', views.home, name='tenant-home'),
    url(r'^mypic/', views.my_pic, name='tenant-mypic'),
    url(r'^pic/', include('avatar.urls')),
)

