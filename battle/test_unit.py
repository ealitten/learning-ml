import unittest

from .models import Pokemon


class TestPokemon(unittest.TestCase):

    def test_pokemon_object(self):
        self.pokemon = Pokemon.objects.create(uid=4, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.name, 'Bulbasaur')

    def test_pokemon_type1(self):
        self.pokemon = Pokemon.objects.create(uid=5, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.type_1, 'grass')

    def test_pokemon_type2(self):
        self.pokemon = Pokemon.objects.create(uid=6, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.type_2, 'poison')

    def test_pokemon_hp(self):
        self.pokemon = Pokemon.objects.create(uid=7, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.hp, 45)

    def test_pokemon_attack(self):
        self.pokemon = Pokemon.objects.create(uid=8, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.attack, 49)

    def test_pokemon_defense(self):
        self.pokemon = Pokemon.objects.create(uid=9, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.defense, 49)

    def test_pokemon_sp_attack(self):
        self.pokemon = Pokemon.objects.create(uid=10, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.sp_attack, 65)

    def test_pokemon_sp_defense(self):
        self.pokemon = Pokemon.objects.create(uid=11, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.sp_defense, 65)

    def test_pokemon_speed(self):
        self.pokemon = Pokemon.objects.create(uid=12, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.speed, 45)

    def test_pokemon_generation(self):
        self.pokemon = Pokemon.objects.create(uid=13, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.generation, 1)

    def test_pokemon_lengendary(self):
        self.pokemon = Pokemon.objects.create(uid=14, name='Bulbasaur', type_1="grass", type_2="poison", hp=45,
                                              attack=49, defense=49, sp_attack=65, sp_defense=65, speed=45, generation=1, lengendary=False)
        self.assertEqual(self.pokemon.lengendary, False)
