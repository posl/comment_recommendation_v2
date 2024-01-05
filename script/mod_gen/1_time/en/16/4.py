def combinationSum4(nums, target):
    n = len(nums)
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(n):
            if i >= nums[j]:
                dp[i] += dp[i - nums[j]]
    return dp[target]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = combinationSum4(nums, target)
    print(a)