from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug:slug>', views.detail, name='detail'),
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('tags/<int:tag_id>', views.list_tags, name='tag'),
]