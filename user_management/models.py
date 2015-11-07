from django.contrib.auth.models import User
from django.db import models

import abc


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __unicode__(self):
        return self.user.username

    @abc.abstractmethod
    def user_type(self):
        return

    class Meta:
        abstract = True
