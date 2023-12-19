def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Approach: Dynamic Programming
    # Intuition:
    # If we have a number n, and we know the number of 1's in its binary representation, say k, then the number of 1's in n + 1 will be k + 1, because n + 1 will have the same number of 1's as n, except for the last bit.
    # Algorithm:
    # Create an array ans of size n + 1, where ans[i] stores the number of 1's in the binary representation of i.
    # Iterate over i from 0 to n.
    # For each i, if i is even, then ans[i] = ans[i / 2], else ans[i] = ans[i / 2] + 1.
    # Return ans.
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 0:
            ans[i] = ans[i // 2]
        else:
            ans[i] = ans[i // 2] + 1
    return ans

if __name__ == '__main__':
    countBits()