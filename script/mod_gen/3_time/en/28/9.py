def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        maxSum = float('-inf')
        currSum = 0
        sums = [float('inf')]
        for i in range(len(arr)):
            currSum += arr[i]
            idx = bisect.bisect_left(sums, currSum - k)
            if idx < len(sums):
                maxSum = max(maxSum, currSum - sums[idx])
            bisect.insort(sums, currSum)
        return maxSum
    
    row, col = len(matrix), len(matrix[0])
    maxSum = float('-inf')
    for i in range(col):
        temp = [0] * row
        for j in range(i, col):
            for r in range(row):
                temp[r] += matrix[r][j]
            maxSum = max(maxSum, maxSumSubarray(temp, k))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()