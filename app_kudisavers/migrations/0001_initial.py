# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('section', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('prodType', models.CharField(max_length=50)),
                ('prodName', models.CharField(max_length=50)),
                ('prodUrl', models.URLField(max_length=100)),
                ('prodProperties', models.TextField(max_length=500)),
                ('brand', models.CharField(max_length=20)),
                ('imageLink', models.URLField(max_length=100)),
                ('image', models.ImageField(upload_to='', max_length=500)),
                ('price', models.FloatField()),
                ('availability', models.CharField(max_length=20)),
                ('discount', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
