# Generated by Django 4.0.3 on 2022-03-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0011_alter_galore_image_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galore',
            name='image_pic',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
