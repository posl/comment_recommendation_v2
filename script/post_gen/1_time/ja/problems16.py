Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[-1]

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i]は、targetがiの時の組み合わせの数
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i]は、iを作るための組み合わせの数
        dp = [0] * (target + 1)
        # 0を作る組み合わせは1通り
        dp[0] = 1

        for i in range(1, target + 1):
            # iを作る組み合わせの数を求める
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        return dp[target]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i]の要素数はtarget+1
        #dp[i]の要素は0
        dp = [0]*(target+1)
        #dp[0]に1を代入
        dp[0] = 1
        #dp[1]に1を代入
        dp[1] = 1
        #dp[2]に2を代入
        dp[2] = 2
        #dp[3]に4を代入
        dp[3] = 4
        #numsの要素を順に取り出す
        for i in range(4, target+1):
            #numsの要素を順に取り出す
            for num in nums:
                #i-numが0以上の場合
                if i-num >= 0:
                    #dp[i]にdp[i]とdp[i-num]の和を代入
                    dp[i] += dp[i-num]
        #dp[target]を返す
        return dp[target]

=======
Suggestion 8

def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]

        return dp[target]
