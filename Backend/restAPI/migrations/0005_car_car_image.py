# Generated by Django 3.2.12 on 2022-03-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0004_user_user_abn'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]