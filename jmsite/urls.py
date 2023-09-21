"""jmsite URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', views.favicon),
    path('', views.home, name='home'),
    path('links/', views.links, name='links'),
    path('blog/', include('blog.urls')),
]
