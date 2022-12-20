from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Post, Tag


def home(request):
    return render(request, 'blog/home.html',)

# def index(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'blog/index.html', context)

class Index(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-published']
    paginate_by = 5

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)

def list_tags(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag_name': tag.name,
        'posts': posts
    }
    return render(request, 'blog/index.html', context)