from django.db import models

class Pokemon(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type_1 = models.CharField(max_length=50,null=True, blank=True)
    type_2 = models.CharField(max_length=50,null=True, blank=True)
    hp = models.PositiveIntegerField(default=0)
    attack = models.PositiveIntegerField(default=0)
    defense = models.PositiveIntegerField(default=0)
    sp_attack = models.PositiveIntegerField(default=0)
    sp_defense = models.PositiveIntegerField(default=0)
    speed = models.PositiveIntegerField(default=0)
    generation = models.PositiveIntegerField(default=0)
    lengendary = models.BooleanField(default=False)


class Predictions(models.Model):
    uid = models.IntegerField(primary_key=True)
    First_pokemon = models.CharField(max_length=50)
    Second_pokemon = models.CharField(max_length=50)
