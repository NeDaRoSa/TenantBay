from django.db import models
from django.contrib.auth.models import User
from user_management.models import Profile


class Tenant(Profile):
    dob = models.DateField()

    def user_type(self):
        return 'tenant'


class Landlord(Profile):
    introduction = models.CharField(max_length=500)

    def user_type(self):
        return 'landlord'
