# Generated by Django 3.2 on 2022-07-16 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20220617_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='fee',
        ),
    ]
