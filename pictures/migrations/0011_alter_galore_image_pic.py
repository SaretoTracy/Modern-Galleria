# Generated by Django 4.0.3 on 2022-03-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0010_galore_image_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galore',
            name='image_pic',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]