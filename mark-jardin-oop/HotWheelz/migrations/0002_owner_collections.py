# Generated by Django 5.0.1 on 2024-01-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotWheelz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='collections',
            field=models.ManyToManyField(to='HotWheelz.collection'),
        ),
    ]
