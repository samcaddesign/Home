# Generated by Django 3.1.7 on 2021-02-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('need_name', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
