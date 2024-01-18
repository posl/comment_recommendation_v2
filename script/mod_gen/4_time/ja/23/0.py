class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        import math
        # 1分間に何回試験できるか
        test_count = minutesToTest // minutesToDie
        # 試験回数は何回になるか
        # 試験回数をNとすると、N^P >= bucketsとなるNの最小値を求める
        # つまり、PlogN >= logbuckets
        # logN >= logbuckets / P
        # N >= buckets^1/P
        # buckets^1/Pを切り上げる
        return math.ceil(math.log(buckets, test_count + 1))

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = Solution()
    print(a.poorPigs(buckets, minutesToDie, minutesToTest))