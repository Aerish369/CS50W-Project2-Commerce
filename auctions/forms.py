from django.forms import ModelForm
from .models import Listings


class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'category', 'bid_price', 'image']
        