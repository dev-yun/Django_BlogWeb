from django import forms
from django.forms import inlineformset_factory

from photo.models import Album, Photo

PhotoInlineFormSet = inlineformset_factory(Album, Photo, fields=['image', 'title', 'description'], extra=2)
# inlineformset은 1:N 관계인 Album과 Photo를 같이 보여주는 폼셋이고 extra 2 는 1앨범당 1포토 + 2포토를 보여주겠다는 의미이다. (즉 3개의 포토)


class PhotoSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')