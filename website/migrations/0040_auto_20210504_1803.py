# Generated by Django 3.1.7 on 2021-05-04 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_softwares_description_4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='need',
        ),
    ]