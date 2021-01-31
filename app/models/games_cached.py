from datetime import datetime

from app.models.game import Game


class GamesCached:
    games = []
    last_update = datetime.now()
    time_to_clean = float(2)
    games_max_len = 250
    last_replaced_position = 0

    def search_game_by_name(self, name):
        return list(filter(lambda x: name in x.name, self.games))

    def search_game_by_name_in_search(self, search_name):
        return list(filter(lambda x: search_name == x.search, self.games))

    def clean(self):
        self.games.clear()

    def check_time_and_clean(self):
        diff = datetime.now() - self.last_update

        if (diff.seconds / 60) >= self.time_to_clean:
            self.last_update = datetime.now()
            self.clean()

    def add_game(self, game: Game):
        """
        Add game to games list. If list has reached the limit (games_max_len) this function
        will overwrite elements in positions specified by last_replaced_position.
        :param game:
        :type Game: Game instance
        :return:
        """
        if len(self.games) == self.games_max_len:
            if self.last_replaced_position == self.games_max_len:
                self.last_replaced_position = 0
            self.games[self.last_replaced_position] = game
            self.last_replaced_position += 1
        else:
            self.games.append(game)

    def add_games(self, games: list):
        for game in games:
            self.add_game(game)
