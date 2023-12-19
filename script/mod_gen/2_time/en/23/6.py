def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    def get_pigs(buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
    return get_pigs(buckets, minutesToDie, minutesToTest)
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1000, 15, 60))
print(poorPigs(1000, 15, 100))
print(poorPigs(1000, 15, 120))
