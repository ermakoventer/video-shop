from django import forms
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Создаем значения для выбора в выпадающем списке
CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))
TYPE_CHOICES = (
    ('Полный пакет', 'full'),
    ('Бесплатный пакет', 'free'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to='user_images')
    mails = models.BooleanField(default=True, verbose_name='Почта')
    sex = models.CharField(choices=CHOICES, default='male', max_length=40)
    account_type = models.CharField(choices=TYPE_CHOICES, default='Бесплатный пакет', max_length=30)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
