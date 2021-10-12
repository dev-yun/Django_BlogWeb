from django import forms


class PhotoSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')