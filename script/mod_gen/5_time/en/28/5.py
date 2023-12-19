def maxSumSubmatrix(matrix, k):
    m, n = len(matrix), len(matrix[0])
    M = max(m, n)
    N = min(m, n)
    ans = float('-inf')
    for x in range(N):
        sums = [0] * M
        for y in range(x, N):
            slist, num = [], 0
            for z in range(M):
                sums[z] += matrix[z][y] if m > n else matrix[y][z]
                num += sums[z]
                if num <= k:
                    ans = max(ans, num)
                i = bisect.bisect_left(slist, num - k)
                if i != len(slist):
                    ans = max(ans, num - slist[i])
                bisect.insort(slist, num)
    return ans

if __name__ == '__main__':
    maxSumSubmatrix()