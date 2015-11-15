from django.contrib import admin
from tenant.models import Tenant
from landlord.models import Landlord

admin.site.register(Tenant)
admin.site.register(Landlord)
