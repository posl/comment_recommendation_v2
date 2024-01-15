#文字列 s を n 回連結した文字列 str を str = [s, n] と定義する。
#例えば、str==["abc", 3] =="abcabcabc"である。
#文字列 s2 からいくつかの文字を削除して文字列 s1 にできる場合、文字列 s1 が文字列 s2 から得られると定義する。
#例えば、太字の下線文字を削除することで、定義に基づき、s1 = "abc"は、s2 = "abdbec"から得ることができる。
#2つの文字列 s1 と s2 、2つの整数 n1 と n2 が与えられ、2つの文字列 str1 = [s1, n1] と str2 = [s2, n2] を有している。
#str1 から str = [str2, m] が得られる最大の整数 m を出力せよ。
#
#例 1：
#入力： s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
#出力： 2
#
#例 2：
#入力： s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
#出力： 1
#
#制約：
#1 <= s1.length, s2.length <= 100
#s1 と s2 は英小文字で構成される。
#1 <= n1, n2 <= 10^6
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int: