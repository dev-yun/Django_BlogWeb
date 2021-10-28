from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from mysite.views import OwnerOnlyMixin
from student.forms import StudentSearchForm
from student.models import Student


class StudentLV(ListView):
    model = Student


class StudentDV(DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['name', 'univ', 'tel', 'group', 'studentnum']
    success_url = reverse_lazy('student:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StudentChangeLV(LoginRequiredMixin, ListView):
    template_name = 'student/student_change_list.html'

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)


class StudentUpdateView(OwnerOnlyMixin, UpdateView):
    model = Student
    fields = ['name', 'univ', 'tel', 'group', 'studentnum']
    success_url = reverse_lazy('student:index')


class StudentDeleteView(OwnerOnlyMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student:index')


class SearchFormView(FormView):
    form_class = StudentSearchForm
    template_name = 'student/student_search.html'

    def get(self, request, *args, **kwargs):
        # Handle GET requests: instantiate a blank version of the form.
        print("get get test")
        context = super().get_context_data(**kwargs)

        student_list = Student.objects.all()

        # context['form'] = self.form_class
        # context['search_term'] = searchWord
        context['object_list'] = student_list

        # return self.render_to_response(self.get_context_data())
        return self.render_to_response(context)
        # return render(self.request, self.template_name, context)

    def form_valid(self, form):
        print(form)
        searchWord = form.cleaned_data['search_word']
        print("post test")
        student_list = Student.objects.filter(
            Q(name__icontains=searchWord) | Q(univ__icontains=searchWord)
            | Q(tel__icontains=searchWord) | Q(group__icontains=searchWord)
            | Q(studentnum__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = student_list

        return render(self.request, self.template_name, context)  # No Redirection
