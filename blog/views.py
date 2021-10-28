from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, \
    DeleteView  # 6장에서 TemplateView추가
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView, TodayArchiveView
from blog.models import Post
from django.conf import settings  # 7장을 위해 추가

from blog.forms import PostSearchForm  # 8장을 위해 추가
from django.db.models import Q  # 8장을 위해 추가
from django.shortcuts import render  # 8장을 위해 추가
from django.views.generic import FormView  # 8장을 위해 추가
from django.views.generic import View  # 8장을 위해 추가


# from blog.forms import PostSearchTestForm  #Test를 위해 추가

# Create your views here.
from mysite.views import OwnerOnlyMixin


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post

    # 7장을위한 코드
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'


# Create your views here.
# --- Tag View   6장에서 추가
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


# --- FormView   8장

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def get(self, request, *args, **kwargs):
        # Handle GET requests: instantiate a blank version of the form.
        print("get get test")
        context = super().get_context_data(**kwargs)

        post_list = Post.objects.all()

        # context['form'] = self.form_class
        # context['search_term'] = searchWord
        context['object_list'] = post_list

        # return self.render_to_response(self.get_context_data())
        return self.render_to_response(context)
        # return render(self.request, self.template_name, context)

    def form_valid(self, form):
        print(form)
        searchWord = form.cleaned_data['search_word']
        print("post test")
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(
            content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)  # No Redirection


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    initial = {'slug': 'auto-filling-dp-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    success_url = reverse_lazy('blog:index')


class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


'''
#--- FormView   Test
class SearchFormViewTest(FormView):
    form_class = PostSearchTestForm
    template_name = 'blog/post_search-test.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        #favorite_colors = form.cleaned_data['favorite_colors']
        #test1 = form.cleaned_data['test1']
        print(self.request.POST.getlist('favorite_colors'))
        favorite_colors = self.request.POST.getlist('favorite_colors')
        print(self.request.POST.getlist('test1'))
        print(self.request.POST.getlist('job'))
        print(self.request.POST.getlist('chk_info'))
        chk_info = self.request.POST.getlist('chk_info')
        #print(favorite_colors)
        #print(test1)
        #https://citylock77.tistory.com/45  카트 예제

        post_list = Post.objects.filter(Q(title__icontains=searchWord) |  Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        context['favorite_colors'] = favorite_colors
        context['chk_info'] = chk_info[0]

        return render(self.request, self.template_name, context)   # No Redirection

'''
