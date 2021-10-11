from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, FormView

from bookmark.forms import BookmarkSearchForm
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class SearchFormView(FormView):
    form_class = BookmarkSearchForm
    template_name = 'bookmark/bookmark_search.html'

    def get(self, request, *args, **kwargs):
        # Handle GET requests: instantiate a blank version of the form.
        print("get get test")
        context = super().get_context_data(**kwargs)

        bookmark_list = Bookmark.objects.all()

        # context['form'] = self.form_class
        # context['search_term'] = searchWord
        context['object_list'] = bookmark_list

        # return self.render_to_response(self.get_context_data())
        return self.render_to_response(context)
        # return render(self.request, self.template_name, context)

    def form_valid(self, form):
        print(form)
        searchWord = form.cleaned_data['search_word']
        print("post test")
        bookmark_list = Bookmark.objects.filter(
            Q(title__icontains=searchWord) | Q(url__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = bookmark_list

        return render(self.request, self.template_name, context)  # No Redirection
