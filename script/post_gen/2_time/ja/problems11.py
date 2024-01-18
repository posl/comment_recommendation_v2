Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i] , dp[j] + 1)
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        # 二分探索
        dp = [0] * len(nums)
        length = 0
        for num in nums:
            # 二分探索
            left = 0
            right = length
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num
            length = max(length, left + 1)
        return length

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        pass

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i] := 長さi+1の増加部分列における最後の要素の最小値
        dp = [float('inf')] * (len(nums) + 1)
        dp[0] = float('-inf')
        for i in range(len(nums)):
            # nums[i]以上の最小値のインデックスを取得
            idx = bisect.bisect_left(dp, nums[i])
            dp[idx] = nums[i]
        
        # dp[i] < inf となる最大のiを返す
        return bisect.bisect_left(dp, float('inf')) - 1

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
