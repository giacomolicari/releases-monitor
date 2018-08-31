# Generated by Django 2.1 on 2018-08-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_management', '0008_auto_20180828_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='last_version',
            field=models.CharField(blank=True, help_text='Supported formats: X.Y.Z, vX.Y.Z, [sometext]X.Y.Z, X.Y.Z[sometext], [sometext]X.Y.Z[sometext], X.Y, vX.Y, [sometext]X.Y, X.Y[sometext], [sometext]X.Y[sometext]', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectlibrary',
            name='check_minor_version_update',
            field=models.BooleanField(default=True, verbose_name='Check Minor Update'),
        ),
        migrations.AlterField(
            model_name='projectlibrary',
            name='check_patch_version_update',
            field=models.BooleanField(default=False, verbose_name='Check Patch Update'),
        ),
        migrations.AlterField(
            model_name='projectlibrary',
            name='current_version',
            field=models.CharField(help_text='Supported formats: X.Y.Z, vX.Y.Z, [sometext]X.Y.Z, X.Y.Z[sometext], [sometext]X.Y.Z[sometext], X.Y, vX.Y, [sometext]X.Y, X.Y[sometext], [sometext]X.Y[sometext]', max_length=20),
        ),
    ]