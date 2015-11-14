from django.core.exceptions import ObjectDoesNotExist
from core.models import Tenant, Landlord


def user_type(user):
    if user.is_authenticated():
        try:
            t = Tenant.objects.get(user=user).user_type()
        except Tenant.DoesNotExist:
            try:
                t = Landlord.objects.get(user=user).user_type()
            except Landlord.DoesNotExist:
                t = 'other'

    else:
        t = 'unauthorised'

    return t
