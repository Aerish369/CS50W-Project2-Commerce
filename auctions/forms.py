from django.forms import ModelForm, widgets
from .models import Listings, Comments

from django import forms


class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'category', 'bid_price', 'image']
    widgets = {
            'in_watchlist':forms.CheckboxSelectMultiple(),
        }

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        