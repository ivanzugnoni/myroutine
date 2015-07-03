# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import routines.models


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0002_auto_20150703_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.CharField(default=routines.models.get_hash_id, max_length=16, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('exercises', models.ManyToManyField(to='routines.Exercise')),
            ],
        ),
    ]
