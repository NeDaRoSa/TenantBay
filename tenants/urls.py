from django.conf.urls import include, url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^tenant/register/', views.register_tenant, name='tenant-register'),
    url(r'^landlord/register/', views.register_landlord, name='landlord-register'),
    url(r'^home/', views.home, name='home')
]
