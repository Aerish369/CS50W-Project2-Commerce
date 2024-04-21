from django.forms import ModelForm, widgets
from .models import Listings, Comments

from django import forms


class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'category', 'bid_price', 'image', 'in_watchlist']
    widgets = {
            'in_watchlist':forms.CheckboxSelectMultiple(),
        }

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        }