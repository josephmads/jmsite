from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.detail, name='detail'),
    path("tags/<int:tag_id>", views.list_tags, name="tag"),
]