# Generated by Django 3.1.7 on 2021-05-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0048_aboutus_description_4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='values',
            name='image',
        ),
        migrations.AddField(
            model_name='values',
            name='description_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='values',
            name='count',
            field=models.CharField(max_length=50),
        ),
    ]