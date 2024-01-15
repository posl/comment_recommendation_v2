#prices[i]が i 日目の株価である配列 prices が与えられる。
#達成できる最大利益を求めよ。ただし，次の制限付きで、好きなだけ取引を行うことができる (1つの株を買っては売ることを複数回繰り返す)：
#株を売却した後、翌日に株を購入することはできない（つまり、クールダウンが1日ある）。
#注意： 複数の取引を同時に行うことはできない（つまり、株を再度購入する前に売却する必要がある）。
#
#例 1：
#入力： prices = [1,2,3,0,2]
#出力： 3
#説明： transactions = [buy, sell, cooldown, buy, sell]
#
#例 2：
#入力： prices = [1]
#出力： 0
#
#制約：
#1 <= prices.length <= 5000
#0 <= prices[i] <= 1000
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
