# Generated by Django 3.2.12 on 2022-09-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='text',
            field=models.CharField(default='', max_length=500),
        ),
    ]
