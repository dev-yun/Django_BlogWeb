from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from mysite.views import OwnerOnlyMixin
from phone.forms import PhoneSearchForm
from phone.models import Phone


class PhoneLV(ListView):
    model = Phone


class PhoneDV(DetailView):
    model = Phone


class PhoneCreateView(LoginRequiredMixin, CreateView):
    model = Phone
    fields = ['name', 'phonenum']
    success_url = reverse_lazy('phone:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PhoneChangeLV(LoginRequiredMixin, ListView):
    template_name = 'phone/phone_change_list.html'

    def get_queryset(self):
        return Phone.objects.filter(owner=self.request.user)


class PhoneUpdateView(OwnerOnlyMixin, UpdateView):
    model = Phone
    fields = ['name', 'phonenum']
    success_url = reverse_lazy('phone:index')


class PhoneDeleteView(OwnerOnlyMixin, DeleteView):
    model = Phone
    success_url = reverse_lazy('phone:index')


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
