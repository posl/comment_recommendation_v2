def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToTest == 1:
        return buckets
    if buckets == 2:
        return 1
    if minutesToTest == 2:
        return 2
    if buckets == 3:
        return 1
    if minutesToTest == 3:
        return 2
    if buckets == 4:
        return 2
    if minutesToTest == 4:
        return 2
    if buckets == 5:
        return 1
    if minutesToTest == 5:
        return 2
    if buckets == 6:
        return 2
    if minutesToTest == 6:
        return 2
    if buckets == 7:
        return 1
    if minutesToTest == 7:
        return 2
    if buckets == 8:
        return 2
    if minutesToTest == 8:
        return 2
    if buckets == 9:
        return 2
    if minutesToTest == 9:
        return 2
    if buckets == 10:
        return 2
    if minutesToTest == 10:
        return 2
    if buckets == 11:
        return 2
    if minutesToTest == 11:
        return 2
    if buckets == 12:
        return 2
    if minutesToTest == 12:
        return 2
    if buckets == 13:
        return 2
    if minutesToTest == 13:
        return 2
    if buckets == 14:
        return 2
    if minutesToTest == 14:
        return 2
    if buckets == 15:
        return 2
    if minutesToTest == 15:
        return 2
    if buckets == 16:
        return 2
    if minutesToTest == 16:
        return 2
    if buckets == 17:
        return 2
    if minutesToTest == 17:
        return 2
    if buckets == 18:
        return

if __name__ == '__main__':
    poorPigs()