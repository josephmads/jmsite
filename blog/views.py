from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView
from .models import *

###########
# Favicon #
###########
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    file = (settings.BASE_DIR / "static" / "favicon.png").open("rb")
    return FileResponse(file)

###############
# End Favicon #
###############


def home(request):
    """View function to display the home page."""
    element = PageElement.objects.get(title='about')
    context = {'element': element}
    # breakpoint()
    return render(request, 'blog/home.html', context)

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

class Links(TemplateView):
    """Class based view to display Links page."""
    template_name = 'blog/links.html'