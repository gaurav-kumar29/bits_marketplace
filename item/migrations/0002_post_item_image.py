# Generated by Django 3.2.5 on 2021-10-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='item_image',
            field=models.ImageField(default='default_item.jpg', upload_to='item_pics'),
        ),
    ]
