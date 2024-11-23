from django.shortcuts import render
from django.views.generic import ListView
from .models import publication

# Create your views here.

class PostListView(ListView):
    model = publication
    template_name = "post_list.html"