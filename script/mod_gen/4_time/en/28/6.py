def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr):
        maxSum = float("-inf")
        prefixSum = 0
        prefixSums = [float("inf")]
        for num in arr:
            bisect.insort(prefixSums, prefixSum)
            prefixSum += num
            i = bisect.bisect_left(prefixSums, prefixSum - k)
            maxSum = max(maxSum, prefixSum - prefixSums[i])
        return maxSum
    maxSum = float("-inf")
    for left in range(len(matrix[0])):
        rowSums = [0] * len(matrix)
        for right in range(left, len(matrix[0])):
            for i in range(len(matrix)):
                rowSums[i] += matrix[i][right]
            maxSum = max(maxSum, maxSumSubarray(rowSums))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()