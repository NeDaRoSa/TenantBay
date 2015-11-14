import user_management
from core.forms import TenantForm


def register(request):
    return user_management.views.register(request, TenantForm, 'user_management/register_tenant.html')


