from django import forms


class PhoneSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')