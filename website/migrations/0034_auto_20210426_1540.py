# Generated by Django 3.1.7 on 2021-04-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_auto_20210426_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]