# Generated by Django 3.2 on 2022-07-16 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
        ('academicyear', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='academic_years', to='institute.institute'),
        ),
    ]
