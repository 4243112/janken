import unittest

# 関数の定義
def judge(computer_hand, player_hand):
    if player_hand == computer_hand:
        print("あいこ")
        return 'draw'
    elif (player_hand == 'グー' and computer_hand == 'チョキ') or \
            (player_hand == 'チョキ' and computer_hand == 'パー') or \
            (player_hand == 'パー' and computer_hand == 'グー'):
        print("あなたの勝ち！")
        return 'player_win'
    else:
        print("あなたの負け...")
        return 'computer_win'

# テストクラスの定義
class TestJudge(unittest.TestCase):

    def test_draw(self):
        self.assertEqual(judge('グー', 'グー'), 'draw')
        self.assertEqual(judge('チョキ', 'チョキ'), 'draw')
        self.assertEqual(judge('パー', 'パー'), 'draw')

    def test_player_win(self):
        self.assertEqual(judge('チョキ', 'グー'), 'player_win')
        self.assertEqual(judge('パー', 'チョキ'), 'player_win')
        self.assertEqual(judge('グー', 'パー'), 'player_win')

    def test_computer_win(self):
        self.assertEqual(judge('グー', 'チョキ'), 'computer_win')
        self.assertEqual(judge('チョキ', 'パー'), 'computer_win')
        self.assertEqual(judge('パー', 'グー'), 'computer_win')

if __name__ == '__main__':
    unittest.main()
