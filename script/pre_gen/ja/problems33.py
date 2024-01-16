#整数配列 nums が与えられたとき、全ての nums の等差な部分列の数を出力せよ。
#数列が等差であるとは，少なくとも3つの要素から構成され、連続する2つの要素間の差が同じものである。
#例えば、[1, 3, 5, 7, 9]、[7, 7, 7, 7]、[3, -1, -5, -9]は等差数列である。
#例えば、[1, 1, 2, 5, 7]は等差数列ではない。
#配列の部分列とは、配列のいくつかの要素（ない場合もある）を取り除いてできる列のことである。
#例えば、[2,5,10] は [1,2,1,2,4,1,5,10] の部分配列である。
#テストケースは、答えが 32 ビット整数に収まるように生成される。
#
#例 1：
#入力： nums = [2,4,6,8,10]
#出力： 7
#説明： すべての等差部分列のスライスは，：
#[2,4,6]
#[4,6,8]
#[6,8,10]
#[2,4,6,8]
#[4,6,8,10]
#[2,4,6,8,10]
#[2,6,10]
#
#例 2：
#入力： nums = [7,7,7,7,7]
#出力： 16
#説明： この配列の任意の部分配列は等差である。
#
#制約：
#1 <= nums.length <= 1000
#-2^31 <= nums[i] <= 2^31 - 1
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int: