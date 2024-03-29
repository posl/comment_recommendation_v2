#異なる単位の硬貨を表す整数配列 coins と、合計金額を表す整数 amount が与えられる。
#その金額を作るのに必要な硬貨の最小の枚数を出力せよ。
#ただし、どの硬貨の組み合わせでもその金額を構成できない場合は、-1を出力せよ。
#各種類の硬貨を無限に持っていると仮定してよい。
#
#例 1：
#入力： coins = [1,2,5], amount = 11
#出力： 3
#説明： 11 = 5 + 5 + 1
#
#例 2：
#入力： coins = [2]、 amount = 3
#出力： -1
#
#例 3：
#入力： coins = [1]、 amount = 0
#出力： 0
#
#制約：
#1 <= coins.length <= 12
#1 <= coins[i] <= 2^31 - 1
#0 <= amount <= 10^4
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int: