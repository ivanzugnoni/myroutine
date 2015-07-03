# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('muscle_group', models.CharField(max_length=100, choices=[(b'pecho', b'Pecho'), (b'espalda', b'Espalda'), (b'biceps', b'Biceps')])),
            ],
        ),
    ]
