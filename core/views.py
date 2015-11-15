from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')

    return render(request, 'index.html', {})


def home(request):
    # if the user is not authenticated, just return to the landing page
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    t = request.user.get_user_type()

    if t is None:
        return HttpResponse('This is page is for actual users')

    return render(request, t + '/home.html', {'user_type': t })


def user_login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')

            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'user_management/login.html', {})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('/')