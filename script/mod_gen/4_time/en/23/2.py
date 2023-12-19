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
        return buckets - 1
    pigs = 1
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
print(poorPigs(1000, 15, 60))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1, 1, 1))
print(poorPigs(1, 1, 2))
print(poorPigs(2, 1, 1))
print(poorPigs(2, 1, 2))
print(poorPigs(4, 1, 1))
print(poorPigs(4, 1, 2))
print(poorPigs(4, 1, 3))
print(poorPigs(4, 1, 4))
print(poorPigs(4, 1, 5))
print(poorPigs(4, 1, 6))
print(poorPigs(4, 1, 7))
print(poorPigs(4, 1, 8))
print(poorPigs(4, 1, 9))
print(poorPigs(4, 1, 10))
print(poorPigs(4, 1, 11))
print(poorPigs(4, 1, 12))
print(poorPigs(4, 1, 13))
print(poorPigs(4, 1, 14))
print(poorPigs(4, 1, 15))
print(poorPigs(4, 1, 16))
print(poorPigs(4, 1, 17))
print(poorPigs(4, 1, 18))
print(poorPigs(4, 1, 19))
print(poorPigs(4, 1, 20))
print(poorPigs(4,
