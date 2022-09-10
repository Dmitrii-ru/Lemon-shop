from django.db import models
from django.utils.text import slugify
from pytils.translit import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=100)
    img = models.ImageField(upload_to='lemon/',blank=True,null=True)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('groups_list', kwargs={'slug': self.slug})
