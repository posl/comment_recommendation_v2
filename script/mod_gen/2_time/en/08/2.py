def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1].
    #F(k+1) = 0 * arr_k[1] + 1 * arr_k[2] + ... + (n - 1) * arr_k[0].
    #F(k+1) - F(k) = 0 * arr_k[1] + 1 * arr_k[2] + ... + (n - 1) * arr_k[0] - 0 * arr_k[0] - 1 * arr_k[1] - ... - (n - 1) * arr_k[n - 1] = 0 * (arr_k[1] - arr_k[0]) + 1 * (arr_k[2] - arr_k[1]) + ... + (n - 1) * (arr_k[0] - arr_k[n - 1])
    #F(k+1) - F(k) = arr_k[1] - arr_k[0] + arr_k[2] - arr_k[1] + ... + arr_k[0] - arr_k[n - 1] = arr_k[0] - arr_k[n - 1]
    #F(k+1) = F(k) + sum(arr) - n * arr_k[n - 1]
    if not nums:
        return 0
    n = len(nums)
    f0 = sum(i * nums[i] for i in range(n))
    s = sum(nums)
    res = f0
    for i in range(1, n):
        f0 += s - n * nums[n - i]
        res = max(res, f0)
    return res

if __name__ == '__main__':
    maxRotateFunction()