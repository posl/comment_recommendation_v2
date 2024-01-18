Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def splitArray(self, nums: list[int], k: int) -> int:
        pass

=======
Suggestion 2

def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.check(nums, mid, k):
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
Suggestion 4

def splitArray(self, nums: list[int], k: int) -> int:
        def check(x):
            cnt = 0
            tmp = 0
            for i in range(n):
                if tmp + nums[i] > x:
                    cnt += 1
                    tmp = nums[i]
                else:
                    tmp += nums[i]
            return cnt + 1 <= k
        n = len(nums)
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
        # 二分探索の初期化
        left = max(nums)
        right = sum(nums)
        # 二分探索
        while left < right:
            mid = (left + right) // 2
            # midが条件を満たすかどうか
            if self.check(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 6

def splitArray(self, nums: list[int], k: int) -> int:
        # 二分探索
        # ある値を決め打ちして、それが条件を満たすかを判定する
        # 条件を満たすなら、それより小さい値で条件を満たすものがあるかを探索する
        # 条件を満たさないなら、それより大きい値で条件を満たすものがあるかを探索する
        # 二分探索の終了条件は、left > right となった場合
        # left が条件を満たす最小の値となる
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(nums, mid, k):
                right = mid - 1
            else:
                left = mid + 1
        return left

=======
Suggestion 7

def splitArray(self, nums: list[int], k: int) -> int:
        def is_ok(arg):
            cnt = 1
            tmp = 0
            for i in range(n):
                if tmp + nums[i] <= arg:
                    tmp += nums[i]
                else:
                    tmp = nums[i]
                    cnt += 1
            return cnt <= k

        n = len(nums)
        left = 0
        right = 0
        for i in range(n):
            left = max(left, nums[i])
            right += nums[i]

        while right - left > 1:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid
            else:
                left = mid

        return right

=======
Suggestion 8

def splitArray(self, nums: list[int], k: int) -> int:
        return 0

=======
Suggestion 9

def splitArray(self, nums: list[int], k: int) -> int:
        # 二分探索
        # 二分探索の範囲は、max(nums) から sum(nums) まで
        # 二分探索の中で、最小値を求める
        # 最小値の求め方は、
        #   1. 二分探索の中で、最小値を仮定する
        #   2. 仮定した最小値を元に、k個のグループに分ける
        #   3. 分けたグループの中で、最大値を求める
        #   4. 最大値が、仮定した最小値より大きければ、仮定した最小値を上げる
        #   5. 最大値が、仮定した最小値より小さければ、仮定した最小値を下げる
        #   6. 1-5を繰り返す
        def check(mid: int) -> bool:
            # 仮定した最小値を元に、k個のグループに分ける
            # 分ける際に、仮定した最小値を超えたら、次のグループにする
            # ただし、グループ数がk個より多い場合は、Falseを返す
            group = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    group += 1
                    total = num
                    if group > k:
                        return False
            return True

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
