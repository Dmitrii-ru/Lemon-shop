from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CHOICES = (('m', "Мужчина  "), ('f', 'Женщина'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    sex = models.CharField('Пол пользователя ',choices=CHOICES, max_length=15, default='m' )
    choi = models.BooleanField(verbose_name='Подписка', default=True, blank=False)

    def __str__(self):
        return f"Профайл пользователя {self.user.username}"

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
