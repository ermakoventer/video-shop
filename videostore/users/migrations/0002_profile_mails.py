# Generated by Django 2.2.7 on 2019-11-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mails',
            field=models.BooleanField(default=True),
        ),
    ]