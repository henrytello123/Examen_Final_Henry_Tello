from django.urls import path
from . import views
urlpatterns = [

   path('profesores_search/', views.Profesores_search, name='profesores_search'),

]