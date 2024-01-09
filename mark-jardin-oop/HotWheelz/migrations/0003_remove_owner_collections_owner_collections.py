# Generated by Django 5.0.1 on 2024-01-09 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotWheelz', '0002_owner_collections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='collections',
        ),
        migrations.AddField(
            model_name='owner',
            name='collections',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HotWheelz.collection'),
        ),
    ]