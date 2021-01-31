import unittest

from app.bot.search import search_game


class TestUtilsFunctions(unittest.TestCase):

    def test_search_game_ok(self):
        game_name = "the-last-of-us-part-2"
        self.assertTrue(search_game(game_name, ""))

    def test_search_game_redirect(self):
        game_name = "gta5"
        self.assertTrue(search_game(game_name, ""))

    def test_search_game_error(self):
        game_name = "Isaac Asimov - El Sol Desnudo"
        self.assertFalse(search_game(game_name, ""))


if __name__ == '__main__':
    unittest.main()
