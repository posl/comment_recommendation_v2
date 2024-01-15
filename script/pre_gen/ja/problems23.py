#液体が入ったバケツが buckets 個あり、そのうちのひとつに毒がある。どのバケツが毒入りかを知るために、あなたは何匹かの（かわいそうな）豚にその液体を飲ませて、死ぬか死なないかを見る。残念なことに、どのバケツが毒入りかを決定するためには、minutesToTest 分しかない。
#次の手順に従って豚に液体を飲ませることができる：
#1.液体を与える生きた豚を選ぶ。
#2.それぞれの豚に、どのバケツを与えるかを選ぶ。豚は同時に選択したすべてのバケツを消費し、時間はかからないものとする。豚は任意の数のバケツを消費でき、バケツは任意の数の豚に与えることができる．
#3.minutesToDie 分待つ。この間、他の豚にバケツを与えてはならない。
#4.minutesToDie 分経過後、毒入りのバケツを与えられた豚は死に、他の豚は生き残る。
#5.時間がなくなるまでこの作業を繰り返す。
#buckets，minutesToDie，minutesToTest が与えられたとき，割り当てられた時間内にどのバケツが毒入りであるかを知るのに必要なブタの最小数を出力せよ。
#
#例 1：
#入力： buckets = 4, minutesToDie = 15, minutesToTest = 15
#出力： 2
#説明： 毒のあるバケツは次のように決定できる：
#時刻0に、最初の豚にバケツ1と2を与え、2番目の豚にバケツ2と3を与える。
#時刻15で、4つの可能な結果がある：
#- もし最初の豚だけが死んだら、バケツ1は毒入りでなければならない。
#- もし2番目の豚だけが死んだら、バケツ3は毒入りでなければならない。
#- もし両方の豚が死んだら、バケツ2は毒入りでなければならない。
#- どちらの豚も死ななければ、バケツ4は毒入りでなければならない。
#
#例 2：
#入力： buckets = 4, minutesToDie = 15, minutesToTest = 30
#出力： 2
#説明： 毒入りのバケツは次のように決定できる：
#時刻0に、最初の豚にバケツ1を与え、2番目の豚にバケツ2を与える。
#時刻15で、2つの可能な結果がある：
#- もしどちらかのブタが死んだら、毒入りのバケツはそのブタに与えられたものである。
#- どちらのブタも死なない場合、最初のブタにバケツ3を与え、2番目のブタにバケツ4を与える。
#時間30で、2匹のブタのどちらかが必ず死に、毒入りのバケツはそのブタに与えられたものである。
#
#制約：
#1 <= buckets <= 1000
#1 <= minutesToDie <= minutesToTest <= 100
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int: