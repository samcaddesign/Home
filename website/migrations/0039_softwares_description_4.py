# Generated by Django 3.1.7 on 2021-05-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20210430_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwares',
            name='description_4',
            field=models.TextField(blank=True),
        ),
    ]