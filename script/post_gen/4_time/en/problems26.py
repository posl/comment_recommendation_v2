Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(self, nums: list[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.is_valid(nums, mid, k):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 2

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    count += 1
                    curr_sum = num
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
Suggestion 3

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            cuts, currSum = 0, 0
            for num in nums:
                currSum += num
                if currSum > mid:
                    cuts, currSum = cuts + 1, num
            return cuts + 1 <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 4

def splitArray(self, nums: list[int], k: int) -> int:
        def isPossible(mid, k):
            curr = 0
            count = 1
            for i in range(len(nums)):
                if nums[i] > mid:
                    return False
                if curr + nums[i] > mid:
                    count += 1
                    curr = nums[i]
                    if count > k:
                        return False
                else:
                    curr += nums[i]
            return True

        left = max(nums)
        right = sum(nums)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid, k):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

=======
Suggestion 5

def splitArray(self, nums: list[int], k: int) -> int:
        def check(m):
            cuts, curr_sum = 0, 0
            for num in nums:
                curr_sum += num
                if curr_sum > m:
                    cuts, curr_sum = cuts + 1, num
            return cuts + 1 <= k
        left, right = max(nums), sum(nums)
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
        def check(mid):
            total = 0
            count = 1
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    count += 1
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
Suggestion 7

def splitArray(self, nums: list[int], k: int) -> int:
        def is_valid(nums, m, k):
            count = 1
            curr_sum = 0
            for i in range(len(nums)):
                if curr_sum + nums[i] > m:
                    count += 1
                    curr_sum = nums[i]
                else:
                    curr_sum += nums[i]
            return count <= k

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if is_valid(nums, mid, k):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 8

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            cuts, curr_sum = 0, 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    cuts, curr_sum = cuts + 1, num
            return cuts + 1 <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

=======
Suggestion 9

def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    current_sum = num
                    count += 1
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 10

def splitArray(self, nums: list[int], k: int) -> int:
        def is_valid_sum(sum_: int) -> bool:
            count = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > sum_:
                    current_sum = num
                    count += 1
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if is_valid_sum(mid):
                right = mid
            else:
                left = mid + 1
        return left
