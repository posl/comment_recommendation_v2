def rotation(nums):
    n = len(nums)
    sum = 0
    for i in range(n):
        sum += i * nums[i]
    max = sum
    for i in range(1, n):
        sum = sum - n * nums[n - i] + sum
        if sum > max:
            max = sum
    return max

if __name__ == '__main__':
    rotation()