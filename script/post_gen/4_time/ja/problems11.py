Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    #dp[i] = max(dp[i], dp[j] + 1)
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i] は i番目の要素を最後とする最長増加部分列の長さ
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # nums[i] より前にある nums[j] が小さい場合
                if nums[j] < nums[i]:
                    # dp[i] の値と dp[j] + 1 の値を比較して大きい方を dp[i] とする
                    dp[i] = max(dp[i], dp[j] + 1)
        # dp の中で最大の値を返す
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        # DP
        # O(n^2)
        # dp[i] := nums[i]までの最長増加部分列
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        # 二分探索
        # dp[i]: 長さが i + 1 の増加部分列の最終要素の最小値
        # dp は必ず単調増加
        # nums[i] が dp の最後尾より大きい場合は dp の最後尾に追加
        # そうでない場合は dp の中で nums[i] より大きい最小の値を nums[i] で置き換える
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                # 二分探索で nums[i] より大きい最小の値を探す
                l, r = 0, len(dp) - 1
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = nums[i]
        return len(dp)

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i] には nums[i] で終わる最長部分列の長さを記録する
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # nums[i] が nums[j] より大きい場合、
                # nums[i] で終わる部分列の長さは
                # nums[j] で終わる部分列の長さの最大値 + 1 となる
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = 1
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
