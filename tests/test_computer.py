import unittest
from unittest.mock import patch
import random

# 関数の定義
def computer_pon():
    hands = ["グー", "チョキ", "パー"]
    computer_hand = random.choice(hands)
    return computer_hand

# テストクラスの定義
class TestComputerPon(unittest.TestCase):

    @patch('random.choice', side_effect=["グー"])
    def test_computer_pon_goo(self, mock_choice):
        self.assertEqual(computer_pon(), "グー")

    @patch('random.choice', side_effect=["チョキ"])
    def test_computer_pon_choki(self, mock_choice):
        self.assertEqual(computer_pon(), "チョキ")

    @patch('random.choice', side_effect=["パー"])
    def test_computer_pon_pa(self, mock_choice):
        self.assertEqual(computer_pon(), "パー")

    def test_computer_pon_random(self):
        for _ in range(100):
            self.assertIn(computer_pon(), ["グー", "チョキ", "パー"])

if __name__ == '__main__':
    unittest.main()
