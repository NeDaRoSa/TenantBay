from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from core.utilities import user_type
from user_management import views


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')

    return render(request, 'index.html', {})


def user_login(request):
    return views.user_login(request)


def user_logout(request):
    return views.user_logout(request)


def home(request):
    # if the user is not authenticated, just return to the landing page
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    t = user_type(request.user)

    if t is 'other':
        return HttpResponse('This is page is for actual users')

    return render(request, t + '/home.html', {'user_type': t })


