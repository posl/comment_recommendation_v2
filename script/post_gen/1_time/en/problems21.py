Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        else:
            count = 0
            for i in range(len(nums)-2):
                diff = nums[i+1] - nums[i]
                for j in range(i+2, len(nums)):
                    if nums[j] - nums[j-1] == diff:
                        count += 1
                    else:
                        break
            return count

=======
Suggestion 3

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 4

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            d = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == d:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 5

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+2,len(nums)):
                diff = nums[i+1] - nums[i]
                if nums[j] - nums[j-1] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j - 1] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # Brute force
        # Time: O(n^3)
        # Space: O(1)
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[j-1]
                flag = True
                for k in range(i+2, j):
                    if nums[k] - nums[k-1] != diff:
                        flag = False
                        break
                if flag:
                    count += 1
        return count

        # Dynamic programming
        # Time: O(n)
        # Space: O(n)
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

        # Dynamic programming
        # Time: O(n)
        # Space: O(1)
        dp = 0
        total = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                total += dp
            else:
                dp = 0
        return total

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        #Solution 1
        #n = len(nums)
        #res = 0
        #for i in range(n-2):
        #    diff = nums[i+1] - nums[i]
        #    for j in range(i+2, n):
        #        if nums[j] - nums[j-1] == diff:
        #            res += 1
        #        else:
        #            break
        #return res
        #Solution 2
        n = len(nums)
        dp = [0]*n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
