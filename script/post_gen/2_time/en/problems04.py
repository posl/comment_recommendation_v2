Synthesizing 9/10 solutions

=======
Suggestion 1

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    for i in range(n+1):
        count = 0
        while i > 0:
            count += i & 1
            i >>= 1
        res.append(count)
    return res

print(countBits(2))
print(countBits(5))
print(countBits(10))
print(countBits(100))
print(countBits(1000))
print(countBits(10000))
print(countBits(100000))
print(countBits(1000000))
print(countBits(10000000))
print(countBits(100000000))
print(countBits(1000000000))
print(countBits(10000000000))
print(countBits(100000000000))
print(countBits(1000000000000))
print(countBits(10000000000000))
print(countBits(100000000000000))
print(countBits(1000000000000000))
print(countBits(10000000000000000))
print(countBits(100000000000000000))
print(countBits(1000000000000000000))
print(countBits(10000000000000000000))
print(countBits(100000000000000000000))
print(countBits(1000000000000000000000))
print(countBits(10000000000000000000000))
print(countBits(100000000000000000000000))
print(countBits(1000000000000000000000000))
print(countBits(10000000000000000000000000))
print(countBits(100000000000000000000000000))
print(countBits(1000000000000000000000000000))
print(countBits(10000000000000000000000000000))
print(countBits(100000000000000000000000000000))
print(countBits(1000000000000000000000000000000))
print(countBits(10000000000000000000000000000000))
print(count

=======
Suggestion 2

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [bin(i).count('1') for i in range(n+1)]

print(countBits(5))
print(countBits(2))
print(countBits(0))
print(countBits(10))
print("The arrays above should be [0, 1, 1, 2, 1, 2], \
    [0, 1, 1], [0], and [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2].")

=======
Suggestion 3

def countBits(n):
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i//2] + (i % 2))
    return ans

print(countBits(2))
print(countBits(5))
print(countBits(0))
print(countBits(1))
print(countBits(10))

=======
Suggestion 4

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    for i in range(n+1):
        res.append(bin(i)[2:].count('1'))
    return res

=======
Suggestion 5

def countBits(n):
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result

=======
Suggestion 6

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # Runtime: 92 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 88 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 96 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 88 ms
    # Memory Usage: 20.7 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 100 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 88 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 88 ms
    # Memory Usage: 20.9 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 88 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 92 ms
    # Memory Usage: 20.7 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 92 ms
    # Memory Usage: 20.8 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 92 ms
    # Memory Usage: 20.7 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 88 ms
    # Memory Usage: 20.7 MB
    # return [bin(i).count('1') for i in range(n+1)]

    # Runtime: 92 ms
    # Memory Usage: 20.8 MB
    # return

=======
Suggestion 7

def countBits(n):
    result = []
    for i in range(n+1):
        result.append(bin(i).count("1"))
    return result

print(countBits(5))

=======
Suggestion 8

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    #return [bin(i).count('1') for i in range(n+1)]
    return [bin(i).count('1') for i in range(n+1)]

print(countBits(2))
print(countBits(5))

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

print(countBits(5))
