def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # TLE
    # def isArithmetic(l):
    #     for i in range(2, len(l)):
    #         if l[i] - l[i-1] != l[1] - l[0]:
    #             return False
    #     return True
    #
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if isArithmetic(l):
    #         return 1
    #     else:
    #         return helper(l[:-1]) + helper(l[1:])
    #
    # return helper(nums)
    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[2:])
    #     else:
    #         return helper(l[1:])
    #
    # return helper(nums)
    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[2:])
    #     else:
    #         return helper(l[1:])
    #
    # return helper(nums)
    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[2:])
    #     else:
    #         return helper(l[1:])
    #
    # return helper(nums)
    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[

if __name__ == '__main__':
    numberOfArithmeticSlices()