from django.db import models
from django.utils.text import slugify
from pytils.translit import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, default="",verbose_name="Название")
    text = models.CharField(max_length=500, default="" ,verbose_name="Описание")
    price = models.IntegerField(default=100, verbose_name='Стоимость')
    img = models.ImageField(upload_to='lemon/',blank=True,null=True,verbose_name='Фото на в карточку')
    slug = models.SlugField(null=False, unique=True)
    readonly_fields = ('slug',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):

        return reverse('detail', kwargs={'slug': self.slug})
