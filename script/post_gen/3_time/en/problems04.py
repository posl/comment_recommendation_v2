Synthesizing 10/10 solutions

=======
Suggestion 1

def countBits(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res

print(countBits(5))

=======
Suggestion 2

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i//2] + i%2)
    return ans


n = 2
print(countBits(n))

n = 5
print(countBits(n))

=======
Suggestion 3

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans

print(countBits(5))

=======
Suggestion 4

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans

n = 5
print(countBits(n))

=======
Suggestion 5

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]
    for i in range(1, n + 1):
        res.append(res[i >> 1] + (i & 1))
    return res

print(countBits(2))
print(countBits(5))

=======
Suggestion 6

def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    result = []
    for i in range(num+1):
        result.append(bin(i).count('1'))
    return result

print(countBits(5))

=======
Suggestion 7

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i >> 1] + (i & 1))
    return ans


print(countBits(5))

=======
Suggestion 8

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

=======
Suggestion 9

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans

=======
Suggestion 10

def countBits(n):
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans

n = 5
print(countBits(n))
