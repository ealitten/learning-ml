from django.test import TestCase
from .models import Pokemon

import unittest

class TestPokemon(unittest.TestCase):

    def test_pokemon_object(self):
        self.pokemon = Pokemon.objects.create(uid=4, name='Bulbasaur',type_1 = "grass",type_2 = "poison",hp = 45,attack = 49,defense = 49,sp_attack = 65,sp_defense = 65,speed = 45,generation = 1,lengendary = False)
        self.assertEqual(self.pokemon.name, 'Bulbasaur')
        self.assertEqual(self.pokemon.type_1, 'grass')
        self.assertEqual(self.pokemon.type_2, 'poison')
        self.assertEqual(self.pokemon.hp, 45)
        self.assertEqual(self.pokemon.attack, 49)
        self.assertEqual(self.pokemon.defense, 49)
        self.assertEqual(self.pokemon.sp_attack, 65)
        self.assertEqual(self.pokemon.sp_defense, 65)
        self.assertEqual(self.pokemon.speed, 45)
        self.assertEqual(self.pokemon.generation, 1)
        self.assertEqual(self.pokemon.lengendary, False)
