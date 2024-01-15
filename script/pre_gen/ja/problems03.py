#整数の rowIndex が与えられたとき、パスカルの三角形の rowIndex 番目の行を出力せよ（0-indexed）。
#パスカルの三角形では、図のように各数値はすぐ上にある2つの数値の和となる：
# 
#例 1：
#入力： rowIndex = 3
#出力： [1,3,3,1]
#
#例 2：
#入力： rowIndex = 0
#出力： [1]
#
#例3：
#入力： rowIndex = 1
#出力： [1,1]
# 
#制約：
#0 <= rowIndex <= 33
#
#フォローアップ： アルゴリズムを最適化し，O(rowIndex)の追加空間しか使わないようにできるか？
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
