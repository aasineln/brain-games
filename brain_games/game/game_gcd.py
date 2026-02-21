import math
import random

from brain_games.game.game_abc import Game


class GCDGame(Game):
    def _get_game_header(self):
        print("Find the greatest common divisor of given numbers.")

    def _generate_question(self) -> dict:
        num_1 = self._get_random_number()
        num_2 = self._get_random_number()

        return {
            "question": f"Question: {num_1} {num_2}",
            "correct_answer": str(self.get_correct_answer(num_1, num_2)),
        }

    @staticmethod
    def get_correct_answer(num_1: int, num_2: int) -> int:
        return math.gcd(num_1, num_2)

    def _check_answer(self, question_data, answer):
        return question_data["correct_answer"] == answer.lower()

    def _get_random_number(self) -> int:
        return random.randint(0, 100)
