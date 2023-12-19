def maxRotateFunction(nums):
    if len(nums) == 1:
        return 0
    else:
        max = 0
        for i in range(len(nums)):
            f = 0
            for j in range(len(nums)):
                f += j * nums[j - i]
            if f > max:
                max = f
        return max

if __name__ == '__main__':
    maxRotateFunction()