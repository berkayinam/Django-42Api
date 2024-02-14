# forms.py
from django import forms

class UserSearchForm(forms.Form):
    search_term = forms.CharField(label='Search for a user', max_length=100)