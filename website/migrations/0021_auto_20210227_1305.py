# Generated by Django 3.1.7 on 2021-02-27 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20210227_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='features',
            old_name='feature_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='feature_name',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='softwares',
            old_name='feature_name',
            new_name='head',
        ),
    ]
