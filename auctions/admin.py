from django.contrib import admin

# Register your models here.

from .models import User, Listings, Bid

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Bid)

