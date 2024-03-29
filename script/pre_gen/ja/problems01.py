#整数の配列 nums と整数 target が与えられたとき、その和がtargetになるような2つの数のインデックスを出力せよ。
#各入力はちょうど1つの解を持つと仮定してよく、同じ要素を2度使ってはならない。
#答えはどの順番で出力しても良い。
#
#例1：
#入力： nums = [2,7,11,15], target = 9
#出力： [0,1]
#説明： nums[0] + nums[1] == 9なので、[0, 1]を返す。
#
#例 2：
#入力： nums = [3,2,4], target = 6
#出力：[1,2]
#
#例3：
#入力： nums = [3,3], ターゲット = 6
#出力： [0,1]
# 
#制約：
#2 <= nums.length <= 10^4
#-10^9 <= nums[i] <= 10^9
#-10^9 <= target <= 10^9
#有効な答えは1つしか存在しない。
#
#フォローアップ：O(n2)未満の時間計算量を持つアルゴリズムで実装できるか？
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: