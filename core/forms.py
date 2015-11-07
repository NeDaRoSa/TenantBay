from django import forms
from django.forms import extras
from datetime import date
from core import models


class TenantForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.extras.widgets.SelectDateWidget(attrs={'class': 'form-control'},
                          years=range(1950, date.today().year - 17)))

    class Meta:
        model = models.Tenant
        fields = ('dob',)


class LandlordForm(forms.ModelForm):
    introduction = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Landlord
        fields = ('introduction',)
