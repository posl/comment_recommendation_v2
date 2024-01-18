Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = dp[i] if dp[i] > dp[j] + 1 else dp[j] + 1
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    #dp[i]はdp[j]の中で最大のものを見つける
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

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
        # dp[i] には i 番目の要素を最後に選んだときの最長部分列の長さを入れる
        dp = [1] * len(nums)
        ans = 0
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    # i 番目の要素を最後に選んだときの最長部分列の長さは
                    # i 番目の要素より前にある j 番目の要素を最後に選んだときの
                    # 最長部分列の長さに 1 を足したものの中で最大のものに 1 を足したもの
                    dp[i] = max(dp[i], dp[j] + 1)
            # i 番目の要素を最後に選んだときの最長部分列の長さが答え
            ans = max(ans, dp[i])
        return ans

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        # 1. nums の長さを取得
        n = len(nums)

        # 2. nums の長さが 1 以下の場合、nums の長さを返却
        if n <= 1:
            return n

        # 3. dp として、nums の長さ分の要素を持つ配列を定義
        dp = [1] * n

        # 4. dp の 2 番目の要素から順に、
        #    dp の i 番目の要素について、
        #    nums の 0 番目から i - 1 番目までの要素について、
        #    nums の i 番目の要素より小さい値を持つ要素のうち、
        #    dp の値が最大のものに 1 を加えた値を代入する
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 5. dp の最大値を返却
        return max(dp)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        # DP
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

        # DP + Binary Search
        dp = [0] * len(nums)
        length = 0
        for num in nums:
            # 二分探索
            left, right = 0, length
            while left < right:
                mid = left + (right-left)//2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num
            length = max(length, left+1)
        return length
