def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    
    def maxSumSubarray(arr, k):
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
    for left in range(n):
        rowSums = [0] * m
        for right in range(left, n):
            for i in range(m):
                rowSums[i] += matrix[i][right]
            maxSum = max(maxSum, maxSumSubarray(rowSums, k))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()