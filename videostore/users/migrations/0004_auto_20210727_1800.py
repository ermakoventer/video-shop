# Generated by Django 3.2.5 on 2021-07-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_sex'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профайл', 'verbose_name_plural': 'Профайлы'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='user_images'),
        ),
    ]
