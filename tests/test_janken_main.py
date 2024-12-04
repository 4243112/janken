import unittest
from unittest.mock import patch
from io import StringIO
import sys

# インポートの統一
import source.player
import source.computer
import source.janken_judge

def main():
    player_win = 0
    computer_win = 0
    rounds = 3

    """3回戦のじゃんけんゲームを行う関数"""
    for round in range(1, rounds + 1):
        print(f"-----ラウンド {round} -----")
        computer_hand = source.computer.computer_pon()
        player_hand = source.player.player_pon()
        result = source.janken_judge.judge(computer_hand, player_hand)

        print(f"あなたの手:{player_hand}")
        print(f"コンピューターの手:{computer_hand}")

        print("")  
        if result == 'draw':
            print("あいこです！ 再度対決！")    
            continue  # Draw の場合は同じラウンドを再度実施
        else:
            if result == 'player_win':
                player_win += 1
                print("あなたの勝ちです！")
            else:
                computer_win += 1
                print("コンピューターの勝ちです！")            

        print("")

    print("【最終結果】")
    print(f"あなた:{player_win}勝")
    print(f"コンピュータ:{computer_win}勝")
    if player_win > computer_win:
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です！")
        

class TestJankenGame(unittest.TestCase):

    @patch('source.player.player_pon', side_effect=['グー', 'チョキ', 'パー'])
    @patch('source.computer.computer_pon', side_effect=['チョキ', 'パー', 'グー'])
    @patch('source.janken_judge.judge', side_effect=['player_win', 'computer_win', 'draw'])
    def test_main(self, mock_judge, mock_computer, mock_player):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Expected output assertions
        self.assertIn("-----ラウンド 1 -----", output)
        self.assertIn("-----ラウンド 2 -----", output)
        self.assertIn("-----ラウンド 3 -----", output)
        self.assertIn("あなたの手:グー", output)
        self.assertIn("コンピューターの手:チョキ", output)
        self.assertIn("あなたの勝ちです！", output)
        self.assertIn("あなたの手:チョキ", output)
        self.assertIn("コンピューターの手:パー", output)
        self.assertIn("コンピューターの勝ちです！", output)
        self.assertIn("あなたの手:パー", output)
        self.assertIn("コンピューターの手:グー", output)
        self.assertIn("あいこです！ 再度対決！", output)
        self.assertIn("【最終結果】", output)
    

if __name__ == '__main__':
    unittest.main()
