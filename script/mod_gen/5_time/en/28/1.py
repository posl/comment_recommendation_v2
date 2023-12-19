def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    import bisect
    def maxSumSubarray(arr, k):
        prefixSum = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            prefixSum[i + 1] = prefixSum[i] + arr[i]
        maxSum = float('-inf')
        for i in range(len(arr)):
            j = bisect.bisect_left(prefixSum, prefixSum[i + 1] - k)
            if j < i + 1:
                maxSum = max(maxSum, prefixSum[i + 1] - prefixSum[j])
        return maxSum
    if len(matrix) > len(matrix[0]):
        matrix = list(zip(*matrix))
    maxSum = float('-inf')
    for i in range(len(matrix)):
        prefixSum = [0 for _ in range(len(matrix[0]))]
        for j in range(i, len(matrix)):
            for l in range(len(matrix[0])):
                prefixSum[l] += matrix[j][l]
            maxSum = max(maxSum, maxSumSubarray(prefixSum, k))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()