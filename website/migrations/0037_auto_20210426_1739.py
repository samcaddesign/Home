# Generated by Django 3.1.7 on 2021-04-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_delete_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='description_3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
