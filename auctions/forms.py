from django.forms import ModelForm, widgets
from .models import Listings

from django import forms


class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'category', 'bid_price', 'image', 'in_watchlist']
    widgets = {
            'in_watchlist':forms.CheckboxSelectMultiple(),
        }
