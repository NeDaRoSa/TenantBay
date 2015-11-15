from django.db import models


class Tenant(models.Model):
    dob = models.DateField()

