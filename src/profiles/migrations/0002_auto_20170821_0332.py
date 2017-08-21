# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country_of_residence',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='national_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='national_id_doc',
            field=models.FileField(null=True, upload_to='national_id'),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='subscription',
            field=models.CharField(choices=[('M', 'Monthly'), ('A', 'Annual')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='town',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='village',
            field=models.CharField(max_length=200, null=True),
        ),
    ]