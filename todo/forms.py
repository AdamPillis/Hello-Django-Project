from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """django based class created for each item"""
    class Meta:
        model = Item
        fields = ['name', 'done']
