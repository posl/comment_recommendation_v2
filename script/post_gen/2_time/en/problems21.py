Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] - nums[i] == nums[i] - nums[i+1]:
                total += 1
        return total

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+2, len(nums)):
                if nums[j]-nums[j-1] == nums[j-1]-nums[j-2]:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 3

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
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
Suggestion 4

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return 0
        count = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count += 1
        return count

=======
Suggestion 5

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return 0
        count = 0
        diff = nums[1] - nums[0]
        curr = 2
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                curr += 1
            else:
                if curr > 2:
                    count += (curr - 1) * (curr - 2) // 2
                curr = 2
                diff = nums[i] - nums[i - 1]
        if curr > 2:
            count += (curr - 1) * (curr - 2) // 2
        return count

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            diff = nums[i+1]-nums[i]
            for j in range(i+1,len(nums)-1):
                if nums[j+1]-nums[j] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                count += 1
                for j in range(2, len(nums)-i):
                    if nums[i+j] - nums[i+j-1] == nums[i+1] - nums[i]:
                        count += 1
                    else:
                        break
        return count

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 9

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2,len(nums)):
                if nums[j] - nums[j-1] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 10

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] != diff:
                    break
                else:
                    count += 1
        return count
