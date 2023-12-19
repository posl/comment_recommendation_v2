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
