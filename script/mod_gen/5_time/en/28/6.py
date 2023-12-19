def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr):
        maxSum = float('-inf')
        prefixSum = 0
        prefixSums = [float('inf')]
        for num in arr:
            bisect.insort(prefixSums, prefixSum)
            prefixSum += num
            i = bisect.bisect_left(prefixSums, prefixSum - k)
            maxSum = max(maxSum, prefixSum - prefixSums[i])
        return maxSum
    maxSum = float('-inf')
    for i in range(len(matrix[0])):
        arr = [0] * len(matrix)
        for j in range(i, len(matrix[0])):
            for k in range(len(matrix)):
                arr[k] += matrix[k][j]
            maxSum = max(maxSum, maxSumSubarray(arr))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()