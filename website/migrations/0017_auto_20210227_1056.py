# Generated by Django 3.1.7 on 2021-02-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20210227_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='position',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='about',
            name='profile',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
