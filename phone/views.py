from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, FormView

from phone.forms import PhoneSearchForm
from phone.models import Phone


class PhoneLV(ListView):
    model = Phone


class PhoneDV(DetailView):
    model = Phone


class SearchFormView(FormView):
    form_class = PhoneSearchForm
    template_name = 'phone/phone_search.html'

    def get(self, request, *args, **kwargs):
        # Handle GET requests: instantiate a blank version of the form.
        print("get get test")
        context = super().get_context_data(**kwargs)

        phone_list = Phone.objects.all()

        # context['form'] = self.form_class
        # context['search_term'] = searchWord
        context['object_list'] = phone_list

        # return self.render_to_response(self.get_context_data())
        return self.render_to_response(context)
        # return render(self.request, self.template_name, context)

    def form_valid(self, form):
        print(form)
        searchWord = form.cleaned_data['search_word']
        print("post test")
        phone_list = Phone.objects.filter(
            Q(name__icontains=searchWord) | Q(phonenum__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = phone_list

        return render(self.request, self.template_name, context)  # No Redirection
