from django import forms


class NamecardSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')