Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

=======
Suggestion 2

def splitArray(self, nums: list[int], k: int) -> int:
        # 二分探索
        # 1. 配列の最大値をleft, 配列の合計をrightとする
        # 2. leftがrightになるまで以下を繰り返す
        #   2-1. leftとrightの中間値をmidとする
        #   2-2. midを最大値としたときに、k個の部分配列に分割できるか判定する
        #   2-3. 可能ならrightをmidに、不可能ならleftをmid+1にする
        # 3. leftを返す
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.isDivided(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 3

def splitArray(self, nums: list[int], k: int) -> int:
        def check(x: int) -> bool:
            cnt = 1
            total = 0
            for num in nums:
                total += num
                if total > x:
                    cnt += 1
                    total = num
            return cnt <= k

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

=======
Suggestion 4

def splitArray(self, nums: list[int], k: int) -> int:
        def check(x: int) -> bool:
            cnt = 1
            total = 0
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= k

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

=======
Suggestion 5

def splitArray(self, nums: list[int], k: int) -> int:
        def check(x):
            cnt = 1
            total = 0
            for num in nums:
                total += num
                if total > x:
                    cnt += 1
                    total = num
            return cnt <= k
        
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left

=======
Suggestion 6

def splitArray(self, nums: list[int], k: int) -> int:
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        # dp[i][j] = min(dp[i][j], max(dp[i][k], sum(k+1, j)))
        dp = [[float('inf')] * len(nums) for _ in range(k)]
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            dp[0][i] = dp[0][i - 1] + nums[i]
        for i in range(1, k):
            for j in range(i, len(nums)):
                for l in range(i - 1, j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][l], sum(nums[l + 1:j + 1])))
        return dp[-1][-1]

=======
Suggestion 7

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # 二分探索
        # 二分探索の範囲は、配列の最大値から配列の合計値まで
        # 二分探索の中で、最大値の最小値を探索する
        # 最大値の最小値を探索するために、
        # 配列をk個に分割したときの、各配列の合計値の最大値を探索する
        # 合計値の最大値が大きいときは、k個に分割したときの配列数が少なくなる
        # 合計値の最大値が小さいときは、k個に分割したときの配列数が多くなる
        # 二分探索の中で、合計値の最大値を探索する
        # 合計値の最大値の最小値がわかれば、それを返せばよい
        # 二分探索の中で、合計値の最大値を探索するときは、
        # その合計値の最大値を超えないように、配列をk個に分割できるかを探索する
        # 配列をk個に分割できるかを探索するときは、
        # その合計値の最大値を超えないように、配列をk個に分割できるかを探索する
        # 配列をk個に分割できるかを探索するときは、
        # その合計値の最大値を超えないように、配列をk個に分割できるかを探索する
        # 配列をk個に分割できるかを探索

=======
Suggestion 8

def splitArray(self, nums: list[int], k: int) -> int:
        pass
        # dp[i][j] = nums[i] + nums[i+1] + ... + nums[j]
        # dp[i][j] = dp[i][j-1] + nums[j]
        # dp[i][j] = dp[i+1][j] - nums[i]
        # dp[i][j] = dp[i+1][j-1] + nums[j] - nums[i]
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i][j-1][k-1] + nums[j] - nums[i])
        # dp[0][n-1][k]
        # dp[i][j][1] = dp[i][j-1][1] + nums[j] - nums[i]
        # dp[i][j][2] = min(dp[i][j][1], dp[i][j-1][2] + nums[j] - nums[i])
        # dp[i][j][3] = min(dp[i][j][2], dp[i][j-1][3] + nums[j] - nums[i])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i][j-1][k-1] + nums[j] - nums[i])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i][j-1][k-1] + nums[j] - nums[i])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i+1][j][k-1] - nums[i])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i+1][j-1][k-1] - nums[i] + nums[j])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i+1][j-1][k-1] - nums[i] + nums[j])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i+1][j-1][k-1] - nums[i] + nums[j])
        # dp[i][j][k] = min(dp[i][j][k-1], dp[i+1][j

=======
Suggestion 9

def splitArray(self, nums: list[int], k: int) -> int:
        # 二分探索
        # 最小値は最大値の最小値となる
        def check(x):
            # xが最小値としたときにk個以上に分割できるか
            cnt = 1
            total = 0
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= k
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
