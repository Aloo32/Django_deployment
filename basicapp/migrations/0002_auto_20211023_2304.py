# Generated by Django 3.2.8 on 2021-10-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='porfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
    ]