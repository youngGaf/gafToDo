# Generated by Django 3.0.6 on 2020-05-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0002_auto_20200528_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
