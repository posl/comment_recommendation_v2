def maxRotateFunction(nums):
    maxSum = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            sum += j * nums[(j + i) % len(nums)]
        if sum > maxSum:
            maxSum = sum
    return maxSum

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = maxRotateFunction(nums)
    print(a)