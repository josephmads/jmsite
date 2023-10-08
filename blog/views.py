from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import *


class Index(ListView):
    """Class based view that lists blog posts and all tags."""
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-published']
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super(Index,self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().order_by('name')
        return context
    
class SearchResults(ListView):
    """Class based view that lists search results"""
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list
    

def detail(request, slug):
    """View function to display blog detail page."""
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)

def list_tags(request, tag_id):
    """View function for displaying tags on blog posts."""
    tag = get_object_or_404(Tag, id=tag_id)
    tags = Tag.objects.all().order_by('name')
    posts = Post.objects.filter(tags=tag).order_by('-published')
    context = {
        'tag_name': tag.name,
        'tags': tags,
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

