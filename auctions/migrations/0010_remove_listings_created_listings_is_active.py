# Generated by Django 5.0.3 on 2024-04-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listings_category_alter_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='created',
        ),
        migrations.AddField(
            model_name='listings',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
