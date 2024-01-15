#異なる正整数 nums の集合が与えられたとき，部分集合の要素のすべての組 (answer[i], answer[j]) が以下を満たすような，最大の部分集合 answer を出力せよ．
#answer[i] % answer[j] == 0, または
#answer[j] % answer[i] == 0
#複数の解がある場合は、それらのいずれかを出力せよ。
#
#例 1：
#入力： nums = [1,2,3]
#出力： [1,2]
#説明： [1,3]も解である。
#
#例 2：
#入力： nums = [1,2,4,8]
#出力： [1,2,4,8]
#
#制約：
#1 <= nums.length <= 1000
#1 <= nums[i] <= 2 * 10^9
#nums の整数はすべて一意である。
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]: