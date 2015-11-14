from core.forms import LandlordForm
import user_management


def register(request):
    return user_management.views.register(request, LandlordForm, 'user_management/register_landlord.html')


