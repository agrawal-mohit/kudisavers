# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_kudisavers', '0002_auto_20150223_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='group',
            new_name='category',
        ),
    ]
