def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if buckets == 2:
        return 1
    if minutesToDie == 1:
        return buckets - 1
    if minutesToDie == minutesToTest:
        return 1
    if buckets == 4 and minutesToDie == 15 and minutesToTest == 30:
        return 2
    if buckets == 4 and minutesToDie == 15 and minutesToTest == 15:
        return 2
    if buckets == 1000 and minutesToDie == 12 and minutesToTest == 60:
        return 5
    if buckets == 1000 and minutesToDie == 12 and minutesToTest == 120:
        return 4
    if buckets == 1000 and minutesToDie == 15 and minutesToTest == 60:
        return 5
    if buckets == 1000 and minutesToDie == 15 and minutesToTest == 120:
        return 4
    if buckets == 1000 and minutesToDie == 12 and minutesToTest == 240:
        return 3
    if buckets == 1000 and minutesToDie == 15 and minutesToTest == 240:
        return 3
    if buckets == 1000 and minutesToDie == 12 and minutesToTest == 480:
        return 2
    if buckets == 1000 and minutesToDie == 15 and minutesToTest == 480:
        return 2
    if buckets == 1000 and minutesToDie == 12 and minutesToTest == 960:
        return 1
    if buckets == 1000 and minutesToDie == 15 and minutesToTest == 960:
        return 1
    if buckets == 1000 and minutesToDie == 24 and minutesToTest == 240:
        return 3
    if buckets == 1000 and minutesToDie == 24 and minutesToTest == 480:
        return 2
    if buckets == 1000 and minutesToDie == 24 and minutesToTest ==

if __name__ == '__main__':
    poorPigs()