def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubArray(arr, k):
        maxSum = float('-inf')
        prefixSum = 0
        prefixSums = [float('inf')]
        for num in arr:
            bisect.insort(prefixSums, prefixSum)
            prefixSum += num
            i = bisect.bisect_left(prefixSums, prefixSum - k)
            maxSum = max(maxSum, prefixSum - prefixSums[i])
        return maxSum
    m, n = len(matrix), len(matrix[0])
    maxSum = float('-inf')
    for i in range(m):
        sums = [0] * n
        for j in range(i, m):
            for c in range(n):
                sums[c] += matrix[j][c]
            maxSum = max(maxSum, maxSumSubArray(sums, k))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()