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

if __name__ == '__main__':
    n = int(input())
    a = countBits(n)
    print(a)