def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1]
    # F(k+1) = 0 * arr_k[1] + 1 * arr_k[2] + ... + (n - 1) * arr_k[0]
    # F(k+1) = F(k) + sum(array) - n * arr_k[n-1]
    # F(k+1) - F(k) = sum(array) - n * arr_k[n-1]
    # F(k+1) = F(k) + sum(array) - n * arr_k[n-1]
    # F(k) = F(k-1) + sum(array) - n * arr_k[n-1]
    # F(k) = F(k-1) + sum(array) - n * arr_k[n-1]
    # F(k-1) = F(k-2) + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) -

if __name__ == '__main__':
    maxRotateFunction()