def countBits(n):
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans
print(countBits(5))
