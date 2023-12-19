def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
buckets = 4
minutesToDie = 15
minutesToTest = 15
print(poorPigs(buckets, minutesToDie, minutesToTest))
buckets = 4
minutesToDie = 15
minutesToTest = 30
print(poorPigs(buckets, minutesToDie, minutesToTest))
