from django.contrib.auth.models import AbstractUser
from django.core.files.storage import get_storage_class
from django.db import models
from landlord.models import Landlord
from tenant.models import Tenant


def picture_path():
    def wrapper(instance, filename):
        extension = filename.split('.')[-1]
        return 'user_images/{0}_avatar.{1}'.format(instance.username, extension)
    return wrapper


class OverwriteStorage(get_storage_class()):
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name):
        return name


class TenantBayUser(AbstractUser):
    tenant_profile = models.OneToOneField(Tenant, null=True, blank=True)
    landlord_profile = models.OneToOneField(Landlord, null=True, blank=True)
    profile_picture = models.ImageField(upload_to=picture_path(), storage=OverwriteStorage())

    def get_user_type(self):
        if self.tenant_profile is not None:
            return 'tenant'
        if self.landlord_profile is not None:
            return 'landlord'
        return None

