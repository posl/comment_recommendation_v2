Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def splitArray(self, nums: list[int], k: int) -> int:
        pass

=======
Suggestion 2

    def splitArray(self, nums: list[int], k: int) -> int:
        # まずは最小値を最大化する問題に変換する
        # 最小値を最大化する問題は二分探索で解ける
        # 二分探索の条件は、
        # 1. 二分探索の最小値を min_val、最大値を max_val とする
        # 2. min_val と max_val の中間値を mid_val とする
        # 3. mid_val が条件を満たすかどうかを判定する
        # 4. 条件を満たす場合は max_val を mid_val に更新する
        # 5. 条件を満たさない場合は min_val を mid_val に更新する
        # 6. min_val と max_val が隣り合ったら、その値が答えになる
        # 今回の条件は、
        # 1. 二分探索の最小値を min_val、最大値を max_val とする
        # 2. min_val と max_val の中間値を mid_val とする
        # 3. mid_val を最小値とした場合の、部分配列の数を cnt とする
        # 4. cnt が k より小さい場合は max_val を mid_val に更新する
        # 5. cnt が k 以上の場合は min_val を mid_val に更新する
        # 6. min_val と max_val が隣り合ったら、その値が答えになる
        # となる
        def check(mid_val: int) -> bool:
            cnt = 1
            tmp = 0
            for num in nums:
                tmp += num
                if tmp > mid_val:
                    tmp = num
                    cnt += 1
                    if cnt > k:
                        return False
            return True
        
        min_val = max(nums)
        max_val = sum(nums)
        while min_val <

=======
Suggestion 3

def splitArray(self, nums: list[int], k: int) -> int:
        return 0

=======
Suggestion 4

def splitArray(self, nums: list[int], k: int) -> int:
        #二分探索
        def check(x):
            cnt = 1
            tmp = 0
            for num in nums:
                if tmp + num > x:
                    cnt += 1
                    tmp = num
                else:
                    tmp += num
            return cnt <= k

        left, right = 0, 10 ** 9
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

=======
Suggestion 5

def splitArray(self, nums: list[int], k: int) -> int:
        def check(x: int) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > x:
                    count += 1
                    total = num
                    if count > k:
                        return False
            return True

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
Suggestion 6

def splitArray(self, nums: list[int], k: int) -> int:
        # dp[i][j] := nums[i]までをj個のグループに分割した時の最大値の最小値
        dp = [[float('inf')] * (k + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 0
        # 累積和
        acc = [0]
        for num in nums:
            acc.append(acc[-1] + num)
        for i in range(len(nums)):
            for j in range(1, k + 1):
                for l in range(i + 1):
                    dp[i + 1][j] = min(dp[i + 1][j], max(dp[l][j - 1], acc[i + 1] - acc[l]))
        return dp[-1][-1]

=======
Suggestion 7

def splitArray(self, nums: list[int], k: int) -> int:
        # 二分探索
        def check(x):
            cnt = 1
            tmp = 0
            for num in nums:
                if tmp + num > x:
                    cnt += 1
                    tmp = num
                else:
                    tmp += num
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
Suggestion 8

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
