Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        diff = 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                diff += 1
                count += diff
            else:
                diff = 0
        return count

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if j - i < 2:
                    continue
                else:
                    if self.isArithmetic(nums[i:j + 1]):
                        res += 1
        return res

=======
Suggestion 3

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
Suggestion 4

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
Suggestion 5

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        i = 0
        while i < n - 2:
            j = i + 1
            diff = nums[j] - nums[i]
            while j < n - 1 and nums[j + 1] - nums[j] == diff:
                j += 1
            length = j - i + 1
            ans += (length - 1) * (length - 2) // 2
            i = j
        return ans

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums) - 2):
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j - 1] == diff:
                    total += 1
                else:
                    break
        return total

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        output = 0
        for i in range(len(nums)-2):
            diff = nums[i+1]-nums[i]
            for j in range(i+2,len(nums)):
                if nums[j]-nums[j-1] == diff:
                    output += 1
                else:
                    break
        return output

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            for j in range(i+2, len(nums)):
                if nums[i+1]-nums[i] == nums[j]-nums[j-1]:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 9

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        start = 0
        end = 2
        count = 0
        while end < len(nums):
            if nums[end]-nums[end-1] == nums[end-1]-nums[end-2]:
                count += 1
                end += 1
            else:
                start += 1
                end += 1
        return count
