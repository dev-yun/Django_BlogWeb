from django import forms


class BookmarkSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')