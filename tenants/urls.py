from django.conf.urls import include, url
from django.contrib import admin

from core import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^tenant/', include('core.tenant_urls')),
    url(r'^landlord/', include('core.landlord_urls')),
    url(r'^usr/', include('user_management.urls'))
]
