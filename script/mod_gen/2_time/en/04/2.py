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
