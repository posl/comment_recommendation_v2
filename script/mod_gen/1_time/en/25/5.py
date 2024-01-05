def solution(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n - 1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = solution(nums)
    print(a)