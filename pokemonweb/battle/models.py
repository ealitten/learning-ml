from django.db import models

class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=50)
