from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('pokemon_data/', views.pokemon_data, name='pokemon_data'),
    path('pokemon_details/', views.pokemon_details, name='pokemon_details'),
    path('fight/', views.fight, name='fight')
]

# from django.urls import url
# from . import views
