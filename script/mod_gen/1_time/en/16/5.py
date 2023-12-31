def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1,target+1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i-num]
    return dp[target]

if __name__ == '__main__':
    self = ==========please modify============
    nums:List[int] = ==========please modify============
    target:int = ==========please modify============
    a = combinationSum4(self, nums: List[int], target: int)
    print(a)