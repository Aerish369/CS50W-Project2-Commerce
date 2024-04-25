from django.contrib import admin

# Register your models here.

from .models import User, Listings, Bid, Comments, Category

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Category)   
admin.site.register(Bid)
admin.site.register(Comments)


