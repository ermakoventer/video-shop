# Generated by Django 2.2.7 on 2019-11-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_mails'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('male', 'Мужской пол'), ('female', 'Женский пол')], default='Мужской пол', max_length=40),
        ),
    ]