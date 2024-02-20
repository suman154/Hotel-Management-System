# Generated by Django 5.0.2 on 2024-02-19 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontdesk', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerroom',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.room'),
        ),
    ]
