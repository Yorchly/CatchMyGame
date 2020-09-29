import unittest

from app.utils import search_in_game_api


class TestUtilsFunctions(unittest.TestCase):

    def test_search_in_game_api_ok(self):
        game_name = "the-last-of-us-part-2"
        self.assertTrue(search_in_game_api(game_name))

    def test_search_in_game_api_redirect(self):
        game_name = "gta5"
        self.assertTrue(search_in_game_api(game_name))

    def test_search_in_game_api_error(self):
        game_name = "Isaac Asimov - El Sol Desnudo"
        self.assertFalse(search_in_game_api(game_name))


if __name__ == '__main__':
    unittest.main()
