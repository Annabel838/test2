# Generated by Django 5.0.3 on 2024-11-03 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='address',
            field=models.CharField(default='No Address Provided', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resident',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resident',
            name='civil_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resident',
            name='contact_number',
            field=models.CharField(default='000-0000-000', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resident',
            name='date_registered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='resident',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Single', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resident',
            name='household_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resident',
            name='occupation',
            field=models.CharField(default='Unemployed', max_length=50),
            preserve_default=False,
        ),
    ]