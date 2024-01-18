Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i + num <= target:
                    dp[i+num] += dp[i]
        return dp[target]

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]

        return dp[target]

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for x in range(1, target + 1):
            for num in nums:
                if x - num >= 0:
                    dp[x] += dp[x - num]
        return dp[target]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i]は合計がiになる組み合わせの数
        dp = [0] * (target + 1)
        # dp[0]は合計が0になる組み合わせは1つ
        dp[0] = 1
        # 0からtargetまでのdpを埋めていく
        for i in range(1, target + 1):
            for num in nums:
                # iより小さい数は足し合わせてiになる組み合わせの数に加算する
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 8

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for n in nums:
                if i + n <= target:
                    dp[i + n] += dp[i]

        return dp[target]

=======
Suggestion 9

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for n in nums:
                if i-n >= 0:
                    dp[i] += dp[i-n]
        return dp[target]
