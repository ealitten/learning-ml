from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('winner/', views.winner, name='winner'),
]
