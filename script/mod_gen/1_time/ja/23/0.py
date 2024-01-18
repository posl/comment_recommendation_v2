class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 2進数で表せる桁数を求める
        # 2^x >= buckets
        # x >= log2(buckets)
        # 2^x >= minutesToTest / minutesToDie + 1
        # x >= log2(minutesToTest / minutesToDie + 1)
        import math
        return math.ceil(math.log2(buckets)) // math.ceil(math.log2(minutesToTest / minutesToDie + 1))

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = Solution()
    print(a.poorPigs(buckets, minutesToDie, minutesToTest))