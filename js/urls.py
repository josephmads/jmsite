from django.urls import path
from js import views

app_name = 'js'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]