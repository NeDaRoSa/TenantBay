from django.shortcuts import render
from core.forms import UserForm
from landlord.forms import LandlordForm


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = LandlordForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save()
            profile.save()
            user = user_form.save()
            user.set_password(user.password)
            user.landlord_profile = profile
            user.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = LandlordForm()

    return render(request, 'user_management/register_landlord.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
