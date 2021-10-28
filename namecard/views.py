from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from mysite.views import OwnerOnlyMixin
from namecard.forms import NamecardSearchForm
from namecard.models import Namecard_TBL


class NamecardLV(ListView):
    model = Namecard_TBL


class NamecardDV(DetailView):
    model = Namecard_TBL


class NamecardCreateView(LoginRequiredMixin, CreateView):
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group']
    success_url = reverse_lazy('namecard:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NamecardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'namecard/namecard_change_list.html'

    def get_queryset(self):
        return Namecard_TBL.objects.filter(owner=self.request.user)


class NamecardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group']
    success_url = reverse_lazy('namecard:index')


class NamecardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Namecard_TBL
    success_url = reverse_lazy('namecard:index')


class SearchFormView(FormView):
    form_class = NamecardSearchForm
    template_name = 'namecard/namecard_search.html'

    def get(self, request, *args, **kwargs):
        # Handle GET requests: instantiate a blank version of the form.
        print("get get test")
        context = super().get_context_data(**kwargs)

        namecard_list = Namecard_TBL.objects.all()

        # context['form'] = self.form_class
        # context['search_term'] = searchWord
        context['object_list'] = namecard_list

        # return self.render_to_response(self.get_context_data())
        return self.render_to_response(context)
        # return render(self.request, self.template_name, context)

    def form_valid(self, form):
        print(form)
        searchWord = form.cleaned_data['search_word']
        print("post test")
        namecard_list = Namecard_TBL.objects.filter(
            Q(name__icontains=searchWord) | Q(tel__icontains=searchWord)
            | Q(company__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = namecard_list

        return render(self.request, self.template_name, context)  # No Redirection
