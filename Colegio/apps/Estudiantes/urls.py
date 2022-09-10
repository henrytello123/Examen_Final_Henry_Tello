from django.urls import path
from . import views
urlpatterns = [
    path('', views.Colegio_list, name='post_list'),
]