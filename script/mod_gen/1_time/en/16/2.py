def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = combinationSum4(nums, target)
    print(a)