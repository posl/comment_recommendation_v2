#カエルが川を渡ろうとしている。川はいくつかの単位に分かれており、各単位には石があってもなくてもよい。カエルは石に飛び乗ることはできるが、水の中に飛び込んではならない。
#石の位置（石が存在する単位）を昇順に並べたリストが与えられたとき、カエルが最後の石に着地して川を渡れるかどうかを判定せよ。最初、カエルは最初の石の上にいて、最初のジャンプは1単位でなければならないと仮定する。
#カエルの最後のジャンプが k 単位であった場合、次のジャンプは k - 1、k、k + 1 単位のいずれかでなければならない。カエルは前進方向にしかジャンプできない．
#
#例 1：
#入力： stones = [0,1,3,5,6,8,12,17]
#出力： true
#説明： カエルは2番目の石に1単位、3番目の石に2単位、4番目の石に2単位、6番目の石に3単位、7番目の石に4単位、8番目の石に5単位跳ぶことによって最後の石に跳ぶことができる。
#
#例 2：
#入力: stones = [0,1,2,3,4,8,9,11]
#出力： false
#説明： 5番目の石と6番目の石の間の間隔が大きすぎるので、最後の石にジャンプする方法はない。
#
#制約：
#2 <= stones.length <= 2000
#0 <= stones[i] <= 2^31 - 1
#stones[0] == 0
#stonesは厳密に増加する順序でソートされます。
class Solution:
    def canCross(self, stones: list[int]) -> bool: