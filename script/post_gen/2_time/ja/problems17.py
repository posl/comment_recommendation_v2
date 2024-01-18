Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 2

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 3

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 4

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

=======
Suggestion 5

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins = sorted(coins)
        for i in range(1, amount + 1):
            for j in coins:
                if i - j < 0:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 6

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # dp[i] := i円を作るのに必要な最小の枚数
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

=======
Suggestion 7

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

=======
Suggestion 8

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

=======
Suggestion 9

def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1
