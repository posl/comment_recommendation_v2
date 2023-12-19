def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # Approach: Dynamic Programming
    # Time Complexity: O(rowIndex^2)
    # Space Complexity: O(rowIndex)
    # rowIndex = 0: [1]
    # rowIndex = 1: [1, 1]
    # rowIndex = 2: [1, 2, 1]
    # rowIndex = 3: [1, 3, 3, 1]
    # rowIndex = 4: [1, 4, 6, 4, 1]
    # rowIndex = 5: [1, 5, 10, 10, 5, 1]
    # rowIndex = 6: [1, 6, 15, 20, 15, 6, 1]
    # rowIndex = 7: [1, 7, 21, 35, 35, 21, 7, 1]
    # rowIndex = 8: [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # rowIndex = 9: [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    # rowIndex = 10: [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    # rowIndex = 11: [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
    # rowIndex = 12: [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]
    # rowIndex = 13: [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]
    # rowIndex = 14: [1, 14, 91, 364, 1001, 2002, 3003, 3432,

if __name__ == '__main__':
    getRow()