#整数配列 nums が与えられたとき、両方の部分集合の要素の和が
#等しくなるように2つの部分集合に分割できればtrueを、そうでなければfalseを出力せよ。
#
#例 1：
#入力： nums = [1,5,11,5]
#出力： true
#説明： 配列は[1,5,5]と[11]に分割できる。
#
#例 2：
#入力： nums = [1,2,3,5]
#出力： false
#説明： 配列は等しい和の部分集合に分割できない。
#
#制約：
#1 <= nums.length <= 200
#1 <= nums[i] <= 100
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
