from django.test import TestCase, Client

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
        self.page.visit('battle/')
        assert self.page.has_text('Welcome to We Predicted That\'s Pokemon Battle!')

    def test_pokemon_page_works(self):
        self.page.visit('battle/')
        self.page.click_link('Your Pokemon Battle')
        assert self.page.has_content('Charmander')

    #def expect_stats_to_appear(self):
    #    self.page.visit('battle/')
    #    self.page.click_link('Your Pokemon Battle')
       # click Charmander
       # assert self.page.has_content('Fire')
       # assert self.page.has_content('Speed: 65')
       # assert self.page.has_content('Attack: 52')

    def test_have_a_battle(self):
        self.page.visit('battle/')
        self.page.click_link('Your Pokemon Battle')
        self.page.select("Bulbasaur", field="pk1")
        self.page.select("Wartortle", field="pk2")
        self.page.click_button("Fight")
        assert self.page.has_content("Bulbasaur wins!")

    def tearDown(self):
       capybara.reset_sessions()
