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
                ('Figures', 'Figues'),
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

        owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        title = models.CharField(max_length=60)
        description = models.TextField(max_length=500, blank=True, null=True)
        category = models.CharField(max_length=60, null=True, blank=True, choices=category)
        bid_price = models.IntegerField(blank=True, null=True)
        image = models.ImageField(null=True, blank=True, upload_to='listing-image')
        created = models.DateTimeField(auto_now_add=True)
        

        def __str__(self):
                return f"{self.id} {self.title}"
        
class Bid(models.Model):
        pass
        # def __str__(self):
        #         return ""
        

class Comments(models.Model):
        pass
        # def __str__(self):
        #     return ""
        