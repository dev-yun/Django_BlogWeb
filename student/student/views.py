from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, FormView

from student.forms import StudentSearchForm
from student.models import Student


class StudentLV(ListView):
    model = Student


class StudentDV(DetailView):
    model = Student


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
            | Q(tel__icontains=searchWord)| Q(group__icontains=searchWord)
        | Q(studentnum__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = student_list

        return render(self.request, self.template_name, context)  # No Redirection