def countBits(n):
    ans = [0]
    for i in range(1, n + 1):
        ans.append(ans[i // 2] + (i & 1))
    return ans
print(countBits(5))
