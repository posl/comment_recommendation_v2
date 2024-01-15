#文字列 base を "abcdefghijklmnopqrstuvwxyz"の無限に循環する文字列と定義する.つまり，base： "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd..." となる。
#文字列 s が与えられたとき、baseに存在する，sの空でない一意な部分文字列の数を出力せよ。
#
#例 1：
#入力： s = "a"
#出力： 1
#説明： sの部分文字列 "a"だけがbaseに入っている。
#
#例2：
#入力： s = "cac"
#出力： 2
#説明： sの部分文字列でbaseに含まれるのはaだけである
#
#例3：
#入力： s = "zab"
#出力： 6
#説明： sの部分文字列でbaseに含まれるのは6つの部分文字列（"z"、"a"、"b"、"za"、"ab"、"zab"）である。
#
#制約：
#1 <= s.length <= 10^5
#sは英小文字からなる。
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int: