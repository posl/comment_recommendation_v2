def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if buckets <= minutesToTest / minutesToDie + 1:
        return 1
    if buckets <= (minutesToTest / minutesToDie + 1) ** 2:
        return 2
    if buckets <= (minutesToTest / minutesToDie + 1) ** 3:
        return 3
    if buckets <= (minutesToTest / minutesToDie + 1) ** 4:
        return 4
    if buckets <= (minutesToTest / minutesToDie + 1) ** 5:
        return 5
    if buckets <= (minutesToTest / minutesToDie + 1) ** 6:
        return 6
    if buckets <= (minutesToTest / minutesToDie + 1) ** 7:
        return 7
    if buckets <= (minutesToTest / minutesToDie + 1) ** 8:
        return 8
    if buckets <= (minutesToTest / minutesToDie + 1) ** 9:
        return 9
    if buckets <= (minutesToTest / minutesToDie + 1) ** 10:
        return 10
    if buckets <= (minutesToTest / minutesToDie + 1) ** 11:
        return 11
    if buckets <= (minutesToTest / minutesToDie + 1) ** 12:
        return 12
    if buckets <= (minutesToTest / minutesToDie + 1) ** 13:
        return 13
    if buckets <= (minutesToTest / minutesToDie + 1) ** 14:
        return 14
    if buckets <= (minutesToTest / minutesToDie + 1) ** 15:
        return 15
    if buckets <= (minutesToTest / minutesToDie + 1) ** 16:
        return 16
    if buckets <= (minutesToTest / minutesToDie + 1) ** 17:
        return 17
    if buckets <= (minutesToTest / minutesToDie + 1) ** 18

if __name__ == '__main__':
    poorPigs()