Synthesizing 10/10 solutions

=======
Suggestion 1

def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]

=======
Suggestion 2

def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0:
            return False
        dp = [[False for _ in range(sum // 2 + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(len(nums)):
            for j in range(sum // 2 + 1):
                if j < nums[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - nums[i]]
        return dp[len(nums)][sum // 2]

=======
Suggestion 3

def canPartition(self, nums: list[int]) -> bool:
        # まずはソートしておく
        nums.sort()
        # 合計値を求める
        total = sum(nums)
        # 合計値が奇数の場合はFalse
        if total % 2 != 0:
            return False
        # 合計値の半分を求める
        half = total // 2
        # まずは最大値が合計値の半分より大きい場合はFalse
        if nums[-1] > half:
            return False
        # 2つの部分集合に分割できるかを返す
        return self.find(nums, half, len(nums) - 1)

=======
Suggestion 4

def canPartition(self, nums: list[int]) -> bool:
        # 1. まずは合計を求める
        sum = 0
        for i in nums:
            sum += i

        # 2. 合計が奇数の場合は分けられないのでFalse
        if sum % 2 != 0:
            return False

        # 3. 合計の半分を求める
        half = sum // 2

        # 4. 0 ～ 合計の半分までの数をリストに入れる
        dp = [0]
        for i in range(1, half+1):
            dp.append(i)

        # 5. numsの数を1つずつ取り出して、dpのリストの数に足していく
        #    足していく際は、dpのリストの数がnumsの数より大きい場合は
        #    dpのリストの数からnumsの数を引いた数のインデックスの数を足す
        #    例えば、numsの数が4でdpのリストの数が5の場合は、dpのリストの数からnumsの数を引いた数のインデックスの数を足す
        #    これを繰り返していき、dpのリストの数がnumsの数になったらTrueを返す
        for i in nums:
            for j in range(half, i-1, -1):
                dp[j] = max(dp[j], dp[j-i]+i)
                if dp[j] == half:
                    return True

        return False

=======
Suggestion 5

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

=======
Suggestion 6

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        dp = [False for _ in range(half+1)]
        dp[0] = True
        for num in nums:
            for i in range(half,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        return dp[half]

=======
Suggestion 7

def canPartition(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return False
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][target]

=======
Suggestion 8

def canPartition(self, nums: list[int]) -> bool:
        # ここに回答を書く
        return False

=======
Suggestion 9

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[target]

=======
Suggestion 10

def canPartition(self, nums: list[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        target = nums_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
