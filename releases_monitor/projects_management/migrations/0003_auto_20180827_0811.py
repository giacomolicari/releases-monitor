# Generated by Django 2.1 on 2018-08-27 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_management', '0002_auto_20180827_0803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'libraries'},
        ),
        migrations.AlterModelOptions(
            name='projectlibrary',
            options={'verbose_name': 'Library of project', 'verbose_name_plural': 'Libraries of projects'},
        ),
    ]