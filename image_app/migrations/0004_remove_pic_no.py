# Generated by Django 2.1.2 on 2018-10-12 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0003_pic_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='no',
        ),
    ]