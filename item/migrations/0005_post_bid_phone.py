# Generated by Django 3.2.5 on 2021-10-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_post_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bid_phone',
            field=models.CharField(default='XXXXXXXXXX', max_length=10),
        ),
    ]
