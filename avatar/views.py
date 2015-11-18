from django.shortcuts import render
from avatar.forms import ImageUploadForm


def upload_picture(request):
    is_success = False

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile_picture = form.cleaned_data['image']
            request.user.save()
            is_success = True
    else:
        form = ImageUploadForm()

    return render(request, 'tenant/upload_pic.html', {'user_type': 'tenant', 'is_success': is_success, 'upload_form': form})

