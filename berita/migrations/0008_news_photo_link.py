# Generated by Django 4.2.1 on 2023-07-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0007_remove_news_photo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo_link',
            field=models.URLField(default=''),
        ),
    ]