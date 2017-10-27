from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from blog.forms import NewBlogForm
from blog.models import Blog


def index(request):
    blog_list = Blog.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'blog/index.html', context)
    # return HttpResponse("This is the index page of the blog")


def detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)


class AboutView(TemplateView):
    template_name = "blog/blog_about.html"


class CreateBlogView(FormView):
    template_name = 'blog/blog_create.html'
    form_class = NewBlogForm
    success_url = '/success/'


def success(request):
    return HttpResponse("success to new a blog!!!! ")


def saveblog(request):
    form = NewBlogForm(request.POST, username=auth.get_user(request))
    if form.is_valid():
        # title = form.cleaned_data['title']
        # content = form.cleaned_data['content']
        # username = auth.get_user(request)
        # blog = Blog(title=title, content=content, username=username)
        # blog.save()
        # new_blog = form.save(commit=False)
        # new_blog.username = request.user  # auth.get_user(request)
        # print(request.username)
        form.save()
        return HttpResponse("title:,content:")
        #return HttpResponseRedirect("blog/personal_center.html")
    else:
        return HttpResponse("form wrong!!!")


def blog_search(request):
    keyword = request.POST.get('blog_name')
    blog_list = Blog.objects.filter(title__contains=keyword)
    context = {'blog_list': blog_list}
    return render(request, 'blog/index.html', context)


def personal_center(request):
    # user = auth.get_user(request)
    # blog_list = Blog.objects.filter(username=user.id)
    blog_list = Blog.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'blog/personal_center.html', context)


def my_blog(request):
    blog_list = Blog.objects.all()
    context = {'blog_list':blog_list}
    return render(request, 'blog/personal_myblog.html', context)
