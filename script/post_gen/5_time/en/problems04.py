Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countBits(n):
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result

print(countBits(5))

=======
Suggestion 2

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    if n == 2:
        return [0,1,1]
    if n == 3:
        return [0,1,1,2]
    if n == 4:
        return [0,1,1,2,1]
    if n == 5:
        return [0,1,1,2,1,2]
    if n == 6:
        return [0,1,1,2,1,2,2]
    if n == 7:
        return [0,1,1,2,1,2,2,3]
    if n == 8:
        return [0,1,1,2,1,2,2,3,1]
    if n == 9:
        return [0,1,1,2,1,2,2,3,1,2]
    if n == 10:
        return [0,1,1,2,1,2,2,3,1,2,2]
    if n == 11:
        return [0,1,1,2,1,2,2,3,1,2,2,3]
    if n == 12:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2]
    if n == 13:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3]
    if n == 14:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3]
    if n == 15:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
    if n == 16:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
    if

=======
Suggestion 3

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    for i in range(n+1):
        res.append(bin(i).count('1'))
    return res

print(countBits(5))

=======
Suggestion 4

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    answer = []
    for i in range(n+1):
        answer.append(bin(i)[2:].count('1'))
    return answer

=======
Suggestion 5

def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    ans = []
    for i in range(num + 1):
        ans.append(bin(i).count('1'))
    return ans

print(countBits(5))

=======
Suggestion 6

def countBits(n):
    ans = []
    for i in range(n+1):
        count = 0
        while i > 0:
            count += i & 1
            i >>= 1
        ans.append(count)
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
    #Solution 1
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).count('1') for i in range(n+1)]

    #Solution 2
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [sum([int(x) for x in bin(i)[2:]]) for i in range(n+1)]

    #Solution 3
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count('1') for i in range(n+1)]

    #Solution 4
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count('1') for i in range(n+1)]

    #Solution 5
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).count('1') for i in range(n+1)]

    #Solution 6
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count('1') for i in range(n+1)]

    #Solution 7
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count('1') for i in range(n+1)]

    #Solution 8
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count('1') for i in range(n+1)]

    #Solution 9
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count('1') for i in range(n+1)]

    #Solution 10
    #Runtime: 88 ms
    #Memory Usage: 20.7 MB
    #return [bin(i).replace('0b','').count

=======
Suggestion 8

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]
    for i in range(1, n+1):
        res.append(res[i >> 1] + i % 2)
    return res

=======
Suggestion 9

def countBits(n):
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(bin(i)[2:].count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(bin(i).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)[2:]).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)[2:]).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)[2:]).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)[2:]).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)[2:]).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    # for i in range(n+1):
    #     ans.append(str(bin(i)[2:]).count('1'))
    # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ans = []
    #
