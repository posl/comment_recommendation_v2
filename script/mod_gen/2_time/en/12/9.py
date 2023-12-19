def largestDivisibleSubset(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        if n == 0:
            return []
        dp = [1] * n
        prev = [-1] * n
        max_index = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = prev[max_index]
        return res[::-1]

if __name__ == '__main__':
    largestDivisibleSubset()