def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = [0]
    # for i in range(1, n+1):
    #     ans.append(ans[i & (i-1)] + 1)
    # return ans
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = [0]
    # for i in range(1, n+1):
    #     ans.append(ans[i >> 1] + (i & 1))
    # return ans
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    ans = [0] * (n+1)
    for i in range(1, n+1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
print(countBits(2))
print(countBits(5))
print(countBits(100))
