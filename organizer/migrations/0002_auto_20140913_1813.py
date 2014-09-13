# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='user_day',
            new_name='day_plan',
        ),
        migrations.AlterField(
            model_name='itemrequirement',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='meal',
            name='generic_foods',
            field=models.ManyToManyField(to=b'organizer.GenericFood', null=True, blank=True),
        ),
    ]
