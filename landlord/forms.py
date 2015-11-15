from django import forms
from landlord import models


class LandlordForm(forms.ModelForm):
    introduction = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Landlord
        fields = ('introduction',)
