def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToDie >= minutesToTest:
        return -1
    if buckets == 2:
        return 1
    else:
        return int(math.ceil(math.log(buckets, 2)))

if __name__ == '__main__':
    poorPigs()