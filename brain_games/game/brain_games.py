from brain_games.game.game_abc import Game


class BrainGames(Game):
    def start(self):
        self._greeting()
        self._get_player_name()

    def _get_game_header(self):
        pass

    def _generate_question(self):
        pass

    def _check_answer(self, question_data, answer):
        pass
