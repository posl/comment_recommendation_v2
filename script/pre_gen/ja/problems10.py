#与えられる配列 intervals の各要素は intervals[i] = [start_i, end_i] の区間の配列で構成されている．
#各要素の残りの区間が重ならないようにするために削除する必要のある区間数の最小値を出力せよ。
#
#例1：
#入力： intervals = [[1,2],[2,3],[3,4],[1,3]].
#出力： 1
#説明： [1,3]を取り除けば、残りの区間は重ならない。
#
#例2：
#入力： intervals = [[1,2],[1,2],[1,2]].
#出力： 2
#説明： 残りの区間を重ならないようにするには、2つの[1,2]を削除する必要がある。
#
#例3：
#入力： intervals = [[1,2],[2,3]]
#出力： 0
#説明： 区間はすでに重なっていないので、削除する必要はない。
#
#制約
#1 <= intervals.length <= 10^5
#intervals[i].length == 2
#-5 * 10^4 <= start_i < end_i <= 5 * 10^4
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
