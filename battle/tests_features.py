import unittest

import capybara
import capybara.dsl

import pokemonweb.wsgi as mywsgi

from .models import Pokemon

capybara.default_max_wait_time = 5
capybara.app = mywsgi.application
capybara.default_driver = "selenium"


class CapybaraTestCase(unittest.TestCase):

    def setUp(self):
        self.page = capybara.dsl.page

    def test_battle_page_works(self):
        self.page.visit('/')
        assert self.page.has_text(
            "Battle your Pokemon!")

    def test_pokemon(self):
        self.pokemon = Pokemon.objects.create(uid=0, name='Charmander')
        self.page.visit('/')
        self.page.select("Charmander", field="pk1")
        assert self.page.has_content('Charmander')

    def test_have_a_battle(self):
        self.pokemon1 = Pokemon.objects.create(
            uid=3, name='Venusaur', type_1="grass")
        self.pokemon2 = Pokemon.objects.create(
            uid=2, name='Ivysaur', type_1="water")
        self.page.visit('/')
        self.page.select("Venusaur", field="pk1")
        self.page.select("Ivysaur", field="pk2")
        self.page.click_button("Let's Battle")
        assert self.page.has_text("Probability Venusaur will win is 44%")
        assert self.page.has_text("Probability Ivysaur will win is 56%")

    def tearDown(self):
        capybara.reset_sessions()
