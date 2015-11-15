from django.db import models


class Landlord(models.Model):
    introduction = models.CharField(max_length=500)
