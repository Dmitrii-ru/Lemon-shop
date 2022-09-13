# Generated by Django 3.2.12 on 2022-09-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_alter_category_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='lemon/', verbose_name='Фото на в карточку'),
        ),
        migrations.AlterField(
            model_name='category',
            name='price',
            field=models.IntegerField(default=100, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='category',
            name='text',
            field=models.CharField(default='', max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Название'),
        ),
    ]
