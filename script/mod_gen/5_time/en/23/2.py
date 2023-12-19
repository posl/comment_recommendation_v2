def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    pigs = 0
    while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
print(poorPigs(1000, 15, 60))
print(poorPigs(1000, 15, 45))
print(poorPigs(1000, 15, 30))
print(poorPigs(1000, 15, 15))
print(poorPigs(1000, 15, 5))
print(poorPigs(1000, 15, 1))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(4, 15, 60))
print(poorPigs(1000, 60, 15))
print(poorPigs(1000, 45, 15))
print(poorPigs(1000, 30, 15))
print(poorPigs(1000, 15, 15))
print(poorPigs(1000, 5, 15))
print(poorPigs(1000, 1, 15))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 30, 15))
print(poorPigs(4, 60, 15))
