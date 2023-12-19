def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1000, 15, 60))
