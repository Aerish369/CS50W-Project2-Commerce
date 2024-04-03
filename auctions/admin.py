from django.contrib import admin

# Register your models here.

from .models import User, Listings

admin.site.register(User)
admin.site.register(Listings)

