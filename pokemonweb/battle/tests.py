from django.test import TestCase, Client
from .models import Pokemon

import capybara
import capybara.dsl
import unittest
import pokemonweb.wsgi as mywsgi



capybara.app = mywsgi.application
capybara.default_driver = "selenium"

class CapybaraTestCase(unittest.TestCase):

    def setUp(self):
        self.page = capybara.dsl.page
        

    def test_battle_page_works(self):
        self.page.visit('index')
        assert self.page.has_text('Welcome to We Predicted That\'s Pokemon Battle!')

    def test_pokemon_page_works(self):
        self.pokemon = Pokemon.objects.create(uid=0, name='Charmander')
        self.page.visit('index')
        self.page.click_link('Your Pokemon Battle')
        print(self.page.body)
        self.page.select("Charmander", field="pk1")
        
        assert self.page.has_content('Charmander')

 view-pokemon-data-from-database
    def test_have_a_battle(self):
       self.page.visit('index')
       self.page.click_link('Your Pokemon Battle')
       self.page.select("Bulbasaur", field="pk1")
       self.page.select("Wartortle", field="pk2")
       self.page.click_button("Fight")
       assert self.page.has_content("Bulbasaur wins!"
    

    def tearDown(self):
       capybara.reset_sessions()
