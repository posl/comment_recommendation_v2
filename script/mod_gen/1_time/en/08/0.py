def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = 0
    for i in range(len(nums)):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(len(nums)-1, 0, -1):
        curr_sum += sum(nums) - len(nums) * nums[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum
print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))
print(maxRotateFunction([-100,100]))
print("The values above should be 26, 0, 330, 0, and 0.")

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = maxRotateFunction(nums)
    print(a)