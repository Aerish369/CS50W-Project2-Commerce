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

        owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        title = models.CharField(max_length=60)
        description = models.TextField(max_length=500, blank=True, null=True)
        category = models.CharField(max_length=60, null=True, blank=True, choices=category)
        bid_price = models.IntegerField(blank=True, null=True)
        image = models.ImageField(null=True, blank=True, upload_to='listing-image', default='listing-image/default.jpg')
        is_active= models.BooleanField(default=True)
        in_watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

        def __str__(self):
                return f"{self.id} - {self.title}"
        
        @property
        def highest_bid(self):
                return Bid.objects.filter(bid_listing=self).order_by('-bid_amount').first()


        
class Bid(models.Model):
        bid_amount = models.IntegerField(default=None)
        bid_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        bid_listing = models.ForeignKey(Listings, on_delete=models.CASCADE, default=None)

        def __str__(self):
                return f"{self.bid_owner} -- {self.bid_amount}"
        

class Comments(models.Model):
        owner= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        listing = models.ForeignKey(Listings, on_delete=models.CASCADE, default=None)
        body = models.TextField(max_length=400, blank=True, null=True)
        created = models.DateTimeField(auto_now_add=True, null=True)


        def __str__(self):
            return f"{self.owner} -- {self.listing}"
        