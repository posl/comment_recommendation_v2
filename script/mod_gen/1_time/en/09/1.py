def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums)%2!=0:
        return False
    else:
        target = sum(nums)/2
        dp = [False for i in range(int(target)+1)]
        dp[0] = True
        for num in nums:
            for i in range(len(dp)-1,-1,-1):
                if dp[i]:
                    dp[i+num] = True
            if dp[-1]:
                return True
        return False

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = canPartition(nums)
    print(a)