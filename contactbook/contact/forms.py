from django import forms
from .models import ContactBook

class ContactBookForm(forms.ModelForm):
    
    class Meta:
        model = ContactBook
        fields = ("image", "mobile_number", "email", "label", "person_name")

class SearchForm(forms.Form):
    search = forms.CharField( max_length=100, required=False)
