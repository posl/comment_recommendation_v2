def maxSumSubmatrix(matrix,k):
    m,n = len(matrix),len(matrix[0])
    ans = float('-inf')
    for i in range(m):
        total = [0] * n
        for j in range(i,m):
            for c in range(n):
                total[c] += matrix[j][c]
            totalSet = [0]
            currSum = 0
            for v in total:
                currSum += v
                idx = bisect.bisect_left(totalSet,currSum-k)
                if idx < len(totalSet):
                    ans = max(ans,currSum-totalSet[idx])
                bisect.insort(totalSet,currSum)
    return ans

if __name__ == '__main__':
    maxSumSubmatrix()