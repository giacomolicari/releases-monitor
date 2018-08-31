# Generated by Django 2.1 on 2018-08-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_management', '0006_auto_20180827_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlibrary',
            name='check_mayor_version_update',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='projectlibrary',
            name='check_minor_version_update',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='projectlibrary',
            name='check_patch_version_update',
            field=models.BooleanField(default=False),
        ),
    ]