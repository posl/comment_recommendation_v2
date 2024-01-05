def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr, k):
        # Find the max sum subarray <= k
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
    ans = float('-inf')
    for i in range(m):
        arr = [0] * n
        for j in range(i, m):
            for c in range(n):
                arr[c] += matrix[j][c]
            ans = max(ans, maxSumSubarray(arr, k))
    return ans

if __name__ == '__main__':
    matrix = ==========please modify============
    k = int(input())
    a = maxSumSubmatrix(matrix, k)
    print(a)