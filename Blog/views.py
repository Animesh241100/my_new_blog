from django.shortcuts import render, redirect
from .models import Article

from django.contrib import messages
from django.http import Http404 
from .forms import ArticleForm



def blog_home_view(request):
    return render(request, 'blogtemp/blog_home.html', {})



def article_detail_view(request, my_id):
    try:
        obj = Article.objects.get(id=my_id)
    except Article.DoesNotExist:
        raise Http404
    my_context = {
        'article_object' : obj

    }
    return render(request, 'blogtemp/article_detail.html', my_context) 



def article_create_view(request):
    my_form = ArticleForm(request.POST or None)

    if my_form.is_valid():
        my_form.save()
        my_form = ArticleForm()
    my_context = {
        'form' : my_form

    }
    messages.info(request, 'A new article created.')
    return render(request, 'blogtemp/article_create.html', my_context)


def article_list_view(request):
    queryset = Article.objects.all()
    my_context = {
        'Object_list': queryset

    }
    return render(request, 'blogtemp/article_list.html', my_context)


def article_delete_view(request, my_id):
    try:
        obj = Article.objects.get(id=my_id)
    except Article.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        obj.delete()
        return redirect('/blogs/all/')
    my_context = {
        'article_object' : obj

    }
    messages.info(request, 'Deleted successfulle, redirecting to the home page.')
    return render(request, 'blogtemp/article_delete.html', my_context)
