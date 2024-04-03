# Generated by Django 5.0.3 on 2024-04-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid_comments_rename_listing_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(blank=True, choices=[('Collectables', 'Collectables & Art'), ('Costumes', 'Costumes'), ('Props', 'Props'), ('Figures', 'Figues'), ('Home', 'Home & Decor'), ('Accessories', 'Accessories & More'), ('Games', 'Games & Puzzles'), ('Gift Cards', 'Gift Cards'), ('Clearance', 'Clearance')], max_length=60, null=True),
        ),
    ]