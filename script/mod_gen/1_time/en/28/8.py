def maxSumSubmatrix(matrix, k):
    import bisect
    m, n = len(matrix), len(matrix[0])
    M, N = max(m, n), min(m, n)
    ans = float('-inf')
    for i in range(N):
        sums = [0] * M
        for j in range(i, N):
            slist, cur = [0], 0
            for k in range(M):
                sums[k] += matrix[k][j] if m > n else matrix[j][k]
                cur += sums[k]
                idx = bisect.bisect_left(slist, cur - k)
                if idx < len(slist): ans = max(ans, cur - slist[idx])
                bisect.insort(slist, cur)
                if ans == k: return ans
    return ans
print(maxSumSubmatrix([[1,0,1],[0,-2,3]], 2)) # 2
print(maxSumSubmatrix([[2,2,-1]], 3)) # 3
print(maxSumSubmatrix([[2,2,-1, 5]], 3)) # 2
print(maxSumSubmatrix([[2,2,-1, 5]], 4)) # 4
print(maxSumSubmatrix([[2,2,-1, 5]], 5)) # 5
print(maxSumSubmatrix([[2,2,-1, 5]], 6)) # 6
print(maxSumSubmatrix([[2,2,-1, 5]], 7)) # 7
print(maxSumSubmatrix([[2,2,-1, 5]], 8)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 9)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 10)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 11)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 12)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 13)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 14)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]],
