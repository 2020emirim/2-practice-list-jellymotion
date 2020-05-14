from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import bookmark


class BookmarkListView(ListView):
    model = bookmark


class BookmarkCreateView(CreateView):
    model = bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
