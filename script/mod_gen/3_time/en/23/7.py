def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToDie == 1:
        return buckets
    if minutesToTest == 1:
        return 1
    pigs = 0
    while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
print(poorPigs(1000, 15, 60))
