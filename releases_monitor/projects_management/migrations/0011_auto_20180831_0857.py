# Generated by Django 2.1 on 2018-08-31 08:57

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('projects_management', '0010_pin_db_tables'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='library',
            table=None,
        ),
        migrations.AlterModelTable(
            name='project',
            table=None,
        ),
        migrations.AlterModelTable(
            name='projectlibrary',
            table=None,
        ),
    ]
