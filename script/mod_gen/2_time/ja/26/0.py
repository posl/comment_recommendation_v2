class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def check(x: int) -> bool:
            # x が条件を満たすかどうか
            # ここから判定
            cnt = 1
            tmp = 0
            for i in range(n):
                if tmp + nums[i] > x:
                    cnt += 1
                    tmp = nums[i]
                else:
                    tmp += nums[i]
            return cnt <= k
        n = len(nums)
        left = max(nums)
        right = sum(nums)
        # 判定
        while right - left > 1:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = Solution()
    print(a.splitArray(nums, k))