# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20170827_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='depcompanyID',
            new_name='depCompanyID',
        ),
        migrations.AlterField(
            model_name='department',
            name='depName',
            field=models.CharField(max_length=45, primary_key=True),
        ),
        migrations.AlterField(
            model_name='right',
            name='rightParentCode',
            field=models.IntegerField(),
        ),
    ]
