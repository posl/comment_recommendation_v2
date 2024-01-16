class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 1 pig can test 5 buckets in 15 minutes
        # 2 pigs can test 5 * 5 buckets in 15 minutes
        # 3 pigs can test 5 * 5 * 5 buckets in 15 minutes
        # 4 pigs can test 5 * 5 * 5 * 5 buckets in 15 minutes
        # 5 pigs can test 5 * 5 * 5 * 5 * 5 buckets in 15 minutes
        # ... so on
        # if the number of buckets is less than 5^pigs, then we can find the poisonous bucket in 15 minutes
        # if the number of buckets is more than 5^pigs, then we can't find the poisonous bucket in 15 minutes
        # so we need to find the smallest number of pigs that can test more than the number of buckets
        pigs = 0
        while (5 ** pigs < buckets):
            pigs += 1
        return pigs

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = Solution()
    print(a.poorPigs(buckets, minutesToDie, minutesToTest))