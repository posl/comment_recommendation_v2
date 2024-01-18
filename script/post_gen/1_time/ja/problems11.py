Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        # 1. 初期条件
        # 2. DPテーブル定義
        # 3. DPテーブル初期化
        # 4. DPループ
        # 5. 答え
        # 1. 初期条件
        N = len(nums)
        if N == 0:
            return 0

        # 2. DPテーブル定義
        dp = [1] * N

        # 3. DPテーブル初期化
        # dp[0] = 1

        # 4. DPループ
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 5. 答え
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        pass

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    print(nums[j], nums[i])
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i] := 長さi+1の増加部分列の最後尾の最小値
        dp = [0] * len(nums)
        dp[0] = nums[0]
        length = 1
        for i in range(1, len(nums)):
            if dp[length - 1] < nums[i]:
                dp[length] = nums[i]
                length += 1
            else:
                # dpを二分探索して更新する
                l = 0
                r = length - 1
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = nums[i]
        return length

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        maxans = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    #print(i,j,nums[i],nums[j],dp[i],dp[j])
                    dp[i] = max(dp[i], dp[j] + 1)
                    #print(i,j,nums[i],nums[j],dp[i],dp[j])
                    maxans = max(maxans, dp[i])
        return maxans

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
