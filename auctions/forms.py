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
    def __init__(self, *args, **kwargs):
        super(ListingsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        