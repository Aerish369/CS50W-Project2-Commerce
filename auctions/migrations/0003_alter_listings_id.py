# Generated by Django 5.0.3 on 2024-04-06 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_listings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
