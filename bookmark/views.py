from django.shortcuts import render
from django.views.generic.list import ListView
from .models import bookmark


class BookmarkListView(ListView):
    model = bookmark
