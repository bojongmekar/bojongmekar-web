# Generated by Django 4.2.1 on 2023-08-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0009_alter_news_photo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo_link',
            field=models.URLField(default='https://www.airspiralo.com/media/products/notfound.png'),
        ),
    ]
