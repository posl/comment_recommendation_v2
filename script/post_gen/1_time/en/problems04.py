Synthesizing 10/10 solutions

=======
Suggestion 1

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]
    for i in range(1,n+1):
        ans.append(ans[i//2]+i%2)
    return ans

print(countBits(5))
print(countBits(2))
print(countBits(0))
print(countBits(1))
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
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result

print(countBits(2))
print(countBits(5))

=======
Suggestion 3

def countBits(n):
    ans = [0]
    for i in range(1, n + 1):
        ans.append(ans[i // 2] + (i & 1))
    return ans

print(countBits(5))

=======
Suggestion 4

def countBits(n):
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i//2] + i%2)
    return ans

print(countBits(5))

=======
Suggestion 5

def countBits(n):
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans

print(countBits(5))

=======
Suggestion 6

def countBits(n):
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i//2] + (i % 2))
    return ans

print(countBits(2))
print(countBits(5))

=======
Suggestion 7

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
Suggestion 8

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result

print(countBits(2))
print(countBits(5))
print(countBits(0))
print(countBits(1))
print(countBits(10))

=======
Suggestion 9

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i>>1] + (i & 1))
    return ans

=======
Suggestion 10

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # 0 0
    # 1 1
    # 2 10
    # 3 11
    # 4 100
    # 5 101
    # 6 110
    # 7 111
    # 8 1000
    # 9 1001
    # 10 1010
    # 11 1011
    # 12 1100
    # 13 1101
    # 14 1110
    # 15 1111
    # 16 10000
    # 17 10001
    # 18 10010
    # 19 10011
    # 20 10100
    # 21 10101
    # 22 10110
    # 23 10111
    # 24 11000
    # 25 11001
    # 26 11010
    # 27 11011
    # 28 11100
    # 29 11101
    # 30 11110
    # 31 11111
    # 32 100000
    # 33 100001
    # 34 100010
    # 35 100011
    # 36 100100
    # 37 100101
    # 38 100110
    # 39 100111
    # 40 101000
    # 41 101001
    # 42 101010
    # 43 101011
    # 44 101100
    # 45 101101
    # 46 101110
    # 47 101111
    # 48 110000
    # 49 110001
    # 50 110010
    # 51 110011
    # 52 110100
    # 53 110101
    # 54 110110
    # 55 110111
    # 56 111000
    # 57 111001
    # 58 111010
    # 59 111011
    # 60 111
