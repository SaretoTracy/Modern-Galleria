# Generated by Django 4.0.3 on 2022-03-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_galore_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galore',
            name='image_pic',
            field=models.ImageField(default='', upload_to='photos/'),
        ),
    ]
