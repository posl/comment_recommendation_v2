class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        import math
        pigs = 0
        while(math.pow((minutesToTest//minutesToDie+1),pigs)<buckets):
            pigs+=1
        return pigs

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = Solution()
    print(a.poorPigs(buckets, minutesToDie, minutesToTest))