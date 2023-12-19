def maxRotateFunction(nums):
    if len(nums) == 1:
        return 0
    max_sum = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(0, len(nums)):
            sum += (j * nums[(j-i) % len(nums)])
        max_sum = max(max_sum, sum)
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()