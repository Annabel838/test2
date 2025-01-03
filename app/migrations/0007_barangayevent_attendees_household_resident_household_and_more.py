# Generated by Django 5.0.3 on 2024-11-09 03:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_resident_address_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangayevent',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='events', to='app.resident'),
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('household_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('head', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='household_head', to='app.resident')),
            ],
        ),
        migrations.AddField(
            model_name='resident',
            name='household',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='app.household'),
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('involved_residents', models.ManyToManyField(related_name='incidents_involved', to='app.resident')),
                ('reported_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_incidents', to='app.resident')),
            ],
        ),
    ]
