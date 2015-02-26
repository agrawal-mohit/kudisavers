# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_kudisavers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='group',
        ),
        migrations.AddField(
            model_name='product',
            name='site',
            field=models.CharField(default='NA', max_length=20),
            preserve_default=False,
        ),
    ]
