# Generated by Django 4.0.3 on 2022-03-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0008_alter_galore_image_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galore',
            name='image_pic',
        ),
    ]
