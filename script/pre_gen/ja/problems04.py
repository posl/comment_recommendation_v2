#整数 n が与えられたとき、長さn + 1の配列 ans を出力せよ。
#ただし，配列 ans の各要素 ans[i]　(0 <= i <= n)は， i を2進数表現に変換したときの，1の個数である．
#
#例1：
#入力： n = 2
#出力：[0,1,1]
#説明：
#0 --> 0
#1 --> 1
#2 --> 10
#
#例 2：
#入力： n = 5
#出力： [0,1,1,2,1,2]
#説明：
#0 --> 0
#1 --> 1
#2 --> 10
#3 --> 11
#4 --> 100
#5 --> 101
#
#制約：
#0 <= n <= 10^5
#
#フォローアップ：
#実行時間O(n log n)の解を出すのは非常に簡単である。線形時間O(n)で、可能ならばシングルパスで実装できるか？
#組み込み関数（C++の__builtin_popcountのようなもの）を使わずに実装できるか？
class Solution:
    def countBits(self, n: int) -> list[int]: