# Generated by Django 2.1.2 on 2018-10-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='i',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
    ]
