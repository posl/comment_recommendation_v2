#「100ゲーム」では、2人のプレイヤーが交互に1から10までの整数のどれかを、合計に加える。最初に合計を100以上にしたプレイヤーの勝ちである．
#もし各プレイヤーが整数を再利用できないようにゲームを変えたらどうなるだろうか？
#例えば、2人のプレーヤーが1から15までの共通の数字プールから重複なしで交互に選び、合計が100以上になるまで足していくとする。
#maxChoosableInteger と desiredTotal の2つの整数が与えられたとき、
#最初に動いたプレイヤーが勝利できる場合はtrueを、そうでない場合はfalseを出力せよ。ただし，両プレイヤーが最適にプレイすると仮定する。
#
#例 1：
#入力： maxChoosableInteger = 10, desiredTotal = 11
#出力： false
#説明：
#最初のプレイヤーがどの整数を選んでも、最初のプレイヤーは負ける。
#最初のプレイヤーは1から10までの整数を選ぶことができる。
#最初のプレイヤーが1を選んだ場合、2番目のプレイヤーは2から10までの整数しか選べない。
#2番目のプレイヤーは10を選んで、合計 = 11 >= desiredTotal となり，勝利する。
#最初のプレイヤーが他の整数を選んだ場合も同じで、常に2番目のプレイヤーが勝つ。
#
#例 2：
#入力: maxChoosableInteger = 10, desiredTotal = 0
#出力: true
#
#例 3：
#入力： maxChoosableInteger = 10, desiredTotal = 1
#出力： true
#
#制約：
#1 <= maxChoosableInteger <= 20
#0 <= desiredTotal <= 300
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
