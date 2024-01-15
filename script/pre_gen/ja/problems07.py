#super ugly number とは、素因数が配列 primes にある正の整数のことである。
#整数 n と整数の配列 primes が与えられたとき、 n 番目の super ugly number を出力せよ。
#ただし，n 番目の super ugly number は 32 ビット符号付き整数に収まることが保証されている。
#
#例 1：
#入力： n = 12, primes = [2,7,13,19]
#出力： 32
#説明： [1,2,4,7,8,13,14,16,19,26,28,32]は、 primes =[2,7,13,19]で構成された最初の12個の super ugly number の列である。
#
#例2：
#入力： n = 1, 素数 = [2,3,5]
#出力： 1
#説明： 1は素因数を持たないので、すべての素因数は配列primes = [2,3,5]に含まれる。
#
#制約：
#1 <= n <= 105
#1 <= primes.length <= 100
#2 <= primes[i] <= 1000
#primes[i]は素数であることが保証される。
#primesの値はすべて一意であり、昇順に並んでいる。
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
