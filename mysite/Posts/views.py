# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib import quote_plus
from django.shortcuts import render ,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect,Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None,request.FILES or None)
    if  form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        #print form.cleaned_data.get("title") ##checking if the form is complete ok
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url()) #incharge of the redirecting after the form is successfuly filled
    context = {
        "form": form,

    }
    return render(request,"post_form.html",context)


def post_detail(request,id=None):
    instance = get_object_or_404(Post,id=id)
    share_url = quote_plus(instance.content)
    context = {
        "instance":instance,
        "share_url":share_url,
    }
    return render(request,"post_detail.html",context)


def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5) #show 20 blog-posts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        #if  the page is not an integer ,show the  first page
        queryset = paginator.page(1)
    except EmptyPage:
        # if the page is out of range (eg  9999), deliver last page of this results
        queryset = paginator.page(paginator.num_pages)



    context = {
        "title":"NEW BLOG",
        "object_list":queryset,
        "page_request_var": page_request_var
    }
    return render(request,"base.html",context)


def post_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)



def post_delete(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("booking:list")
