# Generated by Django 5.0.2 on 2024-02-19 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
        ('frontdesk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontdesk.customer'),
        ),
        migrations.AddField(
            model_name='payment',
            name='bill',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.bill'),
        ),
    ]
