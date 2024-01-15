#整数 numRows が与えられたとき、パスカルの三角形の最初の numRows 行を出力せよ。
#パスカルの三角形では、図のように各数値はすぐ上にある2つの数値の和となる：
#
#例 1：
#入力： numRows = 5
#出力: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#例2：
#入力： numRows = 1
#出力： [[1]]
#
#制約：
#1 <= numRows <= 30
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
