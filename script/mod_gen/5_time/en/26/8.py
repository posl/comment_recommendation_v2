def minmax(nums, k):
    def condition(val):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > val:
                total = num
                count += 1
        return count <= k
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
nums = [7,2,5,10,8]
k = 2
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 2
print(minmax(nums, k))
nums = [1,4,4]
k = 3
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 5
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 1
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 3
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 4
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 5
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 6
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 7
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 8
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 9
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 10
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 11
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 12
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 13

if __name__ == '__main__':
    minmax()