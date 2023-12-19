def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr, k):
        max_sum = float('-inf')
        prefix_sum = 0
        prefix_sums = [float('inf')]
        for num in arr:
            bisect.insort(prefix_sums, prefix_sum)
            prefix_sum += num
            i = bisect.bisect_left(prefix_sums, prefix_sum - k)
            max_sum = max(max_sum, prefix_sum - prefix_sums[i])
        return max_sum
    max_sum = float('-inf')
    for i in range(len(matrix[0])):
        arr = [0] * len(matrix)
        for j in range(i, len(matrix[0])):
            for k in range(len(matrix)):
                arr[k] += matrix[k][j]
            max_sum = max(max_sum, maxSumSubarray(arr, k))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()