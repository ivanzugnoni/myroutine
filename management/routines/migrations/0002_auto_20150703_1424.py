# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import routines.models


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.CharField(default=routines.models.get_hash_id, max_length=16, serialize=False, editable=False, primary_key=True),
        ),
    ]
