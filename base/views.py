from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import PageElement


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)
def favicon(request: HttpRequest) -> HttpResponse:
    file = (settings.BASE_DIR / "static" / "favicon.png").open("rb")
    return FileResponse(file)

def home(request):
    """View function to display the home page."""
    try:
        element = PageElement.objects.get(title='about')
        context = {'element': element}
        return render(request, 'base/home.html', context)
    except PageElement.DoesNotExist as err:
        print('ERROR: ', str(err))
        return render(request, 'base/home.html')
        
class Links(TemplateView):
    """Class based view to display Links page."""
    template_name = 'base/links.html'