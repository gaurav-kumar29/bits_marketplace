# Generated by Django 3.2.5 on 2021-10-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_post_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default='Unsold', max_length=20),
        ),
    ]
