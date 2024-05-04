from django.forms import ModelForm
from django import forms
from .models import *

class new_listForm(ModelForm):
    name = forms.CharField(label="Title",widget=forms.TextInput)
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        'style' : 'width:100%'}))
    price = forms.FloatField(label="Price(US$)")
    CHOICES = (('Categoría 1', 'Categoría 1'),('Option 2', 'Option 2'),)
    category = forms.ChoiceField(widget=forms.Select,choices=CHOICES)
    # image = forms.ImageField(label="Image")
    class Meta:
        model = auctions
        fields = ["name", "description", "price", "category"]