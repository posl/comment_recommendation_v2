#2つの文字列 s と t が与えられたとき、t に等しい s の部分列の数を出力せよ。
#テストケースは、答えが32ビットの符号付き整数に収まるように生成される。
#
#例 1：
#入力： s = "rabbbit", t = "rabbit"
#出力： 3
#説明：
#以下に示すように、sから "rabbit"を生成する方法は3通りある。
#rabbbit
#rabbbit
#rabbbit
#
#例 2：
#入力： s = "babgbag", t = "bag"
#出力： 5
#説明：
#以下に示すように、sから "bag"を生成する方法は5通りある。
#babgbag
#babgbag
#babgbag
#babgbag
#babgbag
#
#制約：
#1 <= s.length, t.length <= 1000
#s と t は英字で構成される。
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
