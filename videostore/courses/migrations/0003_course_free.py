# Generated by Django 3.2.7 on 2021-09-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210920_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]
