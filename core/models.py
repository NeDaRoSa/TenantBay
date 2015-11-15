from django.contrib.auth.models import AbstractUser
from django.db import models
from landlord.models import Landlord
from tenant.models import Tenant


class TenantBayUser(AbstractUser):
    tenant_profile = models.OneToOneField(Tenant, null=True, blank=True)
    landlord_profile = models.OneToOneField(Landlord, null=True, blank=True)

    def get_user_type(self):
        if self.tenant_profile is not None:
            return 'tenant'
        if self.landlord_profile is not None:
            return 'landlord'
        return None
