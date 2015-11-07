from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import TenantForm, LandlordForm
from user_management import views


def index(request):
    return render(request, 'index.html', {})


def register_tenant(request):
    return views.register(request, TenantForm, 'user_management/register_tenant.html')


def register_landlord(request):
    return views.register(request, LandlordForm, 'user_management/register_landlord.html')


def user_login(request):
    return views.user_login(request)


def user_logout(request):
    return views.user_logout(request)


def home(request):
    # if the user is not authenticated, just return to the landing page
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    return render(request)


