from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Announcement, Category, SubCategory,Comentary
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.http import HttpResponse

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

class UserRegisterView(FormView):
    template_name = 'account/registration.html'
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        pass1 = data.pop('password1') # None
        pass2 = data.pop('password2') # None
        form = UserRegistrationForm(request.POST)
        if pass1 != pass2:
            return self.form_invalid(form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponse('New user has been created')

# Announcement

class Ann(ListView):
    model = Announcement
    context_object_name = 'anns'
    template_name = 'app/ann_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs['sub_pk'])
        return queryset


class AnnDetail(DetailView):
    model = Announcement
    context_object_name = 'ann'
    template_name = 'app/ann_detail.html'



class AnnCreate(CreateView):
    model = Announcement
    fields = '__all__'
    success_url = reverse_lazy('subcat_create')
    template_name = 'app/form.html'



class AnnUpdate(UpdateView):
    model = Announcement
    fields = '__all__'
    success_url = reverse_lazy('ann_list')
    template_name = 'app/form.html'



class AnnDelete(DeleteView):
    model = Announcement
    success_url = reverse_lazy('ann_list')
    template_name = 'app/form.html'




#subaegory


class SubCategoryList(ListView):
    model = SubCategory
    context_object_name = 'subcategories'
    template_name = 'app/subcat_list.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs['cat_pk'])
        return queryset


class SubCategoryDetail(DetailView):
    model = SubCategory
    context_object_name = 'subcategory'
    template_name = 'app/subcat_detail.html'


class SubCategoryCreate(CreateView):
    model = SubCategory
    fields = '__all__'
    success_url = reverse_lazy('category_create')
    template_name = 'app/form.html'


class SubCategoryUpdate(UpdateView):
    model = SubCategory
    fields = '__all__'
    success_url = reverse_lazy('subcat_list')
    template_name = 'app/form.html'


class SubCategoryDelete(DeleteView):
    model = SubCategory
    success_url = reverse_lazy('subcat_list')
    template_name = 'app/form.html'


# category


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'app/cat_list.html'


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'app/cat_detail.html'


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('comment_create')
    template_name = 'app/form.html'


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('cat_list')
    template_name = 'app/form.html'


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('cat_list')
    template_name = 'app/form.html'



#commentary


class CommentList(ListView):
    model = Comentary
    context_object_name = 'commentaries'
    template_name = 'app/comment_list.html'


class CommentDetail(DetailView):
    model = Comentary
    context_object_name = 'commentary'
    template_name = 'app/comment_detail.html'


class CommentCreate(CreateView):
    model = Comentary
    fields = '__all__'
    success_url = reverse_lazy('comment_list')
    template_name = 'app/from.html'


class CommentUpdate(UpdateView):
    model = Comentary
    fields = '__all__'
    success_url = reverse_lazy('comment_list')
    template_name = 'app/from.html'


class CommentDelete(DeleteView):
    model = Comentary
    success_url = reverse_lazy('comment_list')
    template_name = 'app/from.html'


#Independence|!!!!!



class Main(TemplateView):
    template_name = 'main/navbar.html'






