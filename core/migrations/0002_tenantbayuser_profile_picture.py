# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantbayuser',
            name='profile_picture',
            field=models.ImageField(default=None, upload_to='./'),
            preserve_default=False,
        ),
    ]
