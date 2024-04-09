from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):

        def __str__(self):
                return f"{self.username}"



class Listings(models.Model):
        category = (
                ('Collectables', 'Collectables & Art'),
                ('Costumes', 'Costumes'),
                ('Props', 'Props'),
                ('Figures', 'Figures'),
                ('Home', 'Home & Decor'),
                ('Accessories', 'Accessories & More'),
                ('Games', 'Games & Puzzles'), 
                ('Gift Cards', 'Gift Cards'),
                ('Clearance', 'Clearance'),

        )
        watchlist = (
                ('True', 'True'),
                ('False', 'False'),
                ('None', 'None'),
        )

        owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        title = models.CharField(max_length=60)
        description = models.TextField(max_length=500, blank=True, null=True)
        category = models.CharField(max_length=60, null=True, blank=True, choices=category)
        bid_price = models.IntegerField(blank=True, null=True)
        image = models.ImageField(null=True, blank=True, upload_to='listing-image')
        is_active= models.BooleanField(default=True)
        in_watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

        def __str__(self):
                return f"{self.title} by {self.owner}"


        
class Bid(models.Model):
        bid_amount = models.IntegerField(default=None)
        bid_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        bid_listing = models.ForeignKey(Listings, on_delete=models.CASCADE, default=None)

        def __str__(self):
                return f"{self.bid_owner} -- {self.bid_amount}"
        

class Comments(models.Model):
        pass
        # def __str__(self):
        #     return ""
        