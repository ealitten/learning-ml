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

    def test_battle_index_page_works(self):
        self.page.visit('battle')
        assert self.page.has_text('Hello, world')

    def tearDown(self):
        capybara.reset_sessions()

