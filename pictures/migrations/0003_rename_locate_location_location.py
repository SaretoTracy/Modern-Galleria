# Generated by Django 4.0.3 on 2022-03-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_galore_location_delete_galleria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='locate',
            new_name='location',
        ),
    ]
