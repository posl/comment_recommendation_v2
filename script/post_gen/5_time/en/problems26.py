Synthesizing 9/10 solutions

=======
Suggestion 1

def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = l + (r - l) // 2
            if self.valid(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        return l

=======
Suggestion 2

def splitArray(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if k == 1:
            return sum(nums)
        if k == len(nums):
            return max(nums)
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = (l+r)//2
            if self.check(nums, mid, k):
                r = mid
            else:
                l = mid + 1
        return l

=======
Suggestion 3

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            count = 0
            curr_sum = 0
            for i in range(len(nums)):
                if nums[i] > mid:
                    return False
                if curr_sum + nums[i] > mid:
                    count += 1
                    curr_sum = nums[i]
                else:
                    curr_sum += nums[i]
            return count + 1 <= k
        left, right = max(nums), sum(nums)
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
        def isPossible(mid: int) -> bool:
            curr_sum, groups = 0, 1
            for num in nums:
                if curr_sum + num > mid:
                    groups += 1
                    curr_sum = num
                    if groups > k:
                        return False
                else:
                    curr_sum += num
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right-left)//2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 5

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
            count = 1
            total = 0
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
        n = len(nums)
        dp = [[float('inf')]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0
        sub = [0]
        for num in nums:
            sub.append(sub[-1]+num)
        for i in range(1,n+1):
            for j in range(1, min(i,k)+1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[p][j-1], sub[i]-sub[p]))
        return dp[-1][-1]

=======
Suggestion 8

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k
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
Suggestion 9

def splitArray(self, nums: list[int], k: int) -> int:
        #print(nums)
        #print(k)
        def countGroups(nums, maxSum):
            count = 1
            currentSum = 0
            for num in nums:
                if currentSum + num > maxSum:
                    count += 1
                    currentSum = num
                else:
                    currentSum += num
            return count
        
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left)//2
            count = countGroups(nums, mid)
            #print(count)
            if count > k:
                left = mid + 1
            else:
                right = mid
        return left
