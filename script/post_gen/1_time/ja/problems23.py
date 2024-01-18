Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 2進数で表せる桁数を求める
        # 2^x >= buckets
        # x >= log2(buckets)
        # 2^x >= minutesToTest / minutesToDie + 1
        # x >= log2(minutesToTest / minutesToDie + 1)
        import math
        return math.ceil(math.log2(buckets)) // math.ceil(math.log2(minutesToTest / minutesToDie + 1))

=======
Suggestion 2

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1))

=======
Suggestion 3

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 1匹のブタが生き残る時間は minutesToTest / minutesToDie + 1
        # 1匹のブタが生き残れる回数は minutesToTest / minutesToDie
        # 1匹のブタが生き残れる回数の数が buckets より多い数のブタが生き残ることができる
        # なので buckets を minutesToTest / minutesToDie で対数を取る
        return math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1))

=======
Suggestion 4

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        if minutesToTest//minutesToDie == 0:
            return 1
        else:
            return math.ceil(math.log(buckets,minutesToTest//minutesToDie+1))

=======
Suggestion 5

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest // minutesToDie + 1))

=======
Suggestion 6

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # (minutesToTest / minutesToDie + 1) ** pigs >= buckets
        # (minutesToTest / minutesToDie + 1) ** pigs = buckets
        # pigs = log(buckets) / log(minutesToTest / minutesToDie + 1)
        # return ceil(log(buckets) / log(minutesToTest / minutesToDie + 1))
        return ceil(log(buckets, minutesToTest / minutesToDie + 1))

=======
Suggestion 7

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 1匹の豚が生き残れる時間は minutesToTest / minutesToDie + 1
        # 1匹の豚が生き残れる時間を n とすると、n**x >= buckets となる最小の x が答え
        n = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets, n))

=======
Suggestion 8

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        #考え方
        #毒入りのバケツが1つの場合
        #1分間に1匹のブタが飲むことができるバケツの数は5個（1分間に5個のバケツを飲むことができる）
        #毒入りのバケツが2つの場合
        #1分間に1匹のブタが飲むことができるバケツの数は5個（1分間に5個のバケツを飲むことができる）
        #毒入りのバケツが3つの場合
        #1分間に1匹のブタが飲むことができるバケツの数は5個（1分間に5個のバケツを飲むことができる）
        #毒入りのバケツが4つの場合
        #1分間に1匹のブタが飲むことができるバケツの数は5個（1分間に5個のバケツを飲むことができる）
        #毒入りのバケツが5つの場合
        #1分間に1匹のブタが飲むことができるバケツの数は5個（1分間に5個のバケツを飲むことができる）
        #毒入りのバケツが6つの場合
        #1分間に1匹のブタが飲むことができるバケツの数は5個（1分間に5個のバケツを飲むことができる）
        #毒入りのバケツが7つの場合

=======
Suggestion 9

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, n + 1))
