# Generated by Django 3.1.7 on 2021-04-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_auto_20210426_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwares',
            name='description_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='softwares',
            name='image_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]