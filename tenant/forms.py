from django import forms
from django.forms import extras
from datetime import date
from core.forms import UserForm
from tenant import models


class TenantForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.extras.widgets.SelectDateWidget(attrs={'class': 'form-control'},
                          years=range(1950, date.today().year - 17)))

    class Meta:
        fields = ('dob',)
        model = models.Tenant

