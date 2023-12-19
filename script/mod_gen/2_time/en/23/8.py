def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToTest <= minutesToDie:
        return -1
    pigs = 1
    while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
print(poorPigs(4, 15, 15)) #2
print(poorPigs(4, 15, 30)) #2
print(poorPigs(1, 1, 1)) #0
print(poorPigs(1000, 15, 60)) #5
print(poorPigs(1000, 12, 60)) #4
print(poorPigs(1000, 1, 60)) #9
print(poorPigs(1000, 1, 100)) #9
print(poorPigs(1000, 1, 1000)) #9
print(poorPigs(1000, 1, 10000)) #9
print(poorPigs(1000, 1, 100000)) #9
print(poorPigs(1000, 1, 1000000)) #9
print(poorPigs(1000, 1, 10000000)) #9
print(poorPigs(1000, 1, 100000000)) #9
print(poorPigs(1000, 1, 1000000000)) #9
print(poorPigs(1000, 1, 10000000000)) #9
print(poorPigs(1000, 1, 100000000000)) #9
print(poorPigs(1000, 1, 1000000000000)) #9
print(poorPigs(1000, 1, 10000000000000)) #9
print(poorPigs(1000, 1, 100000000000000)) #9
print(poorPigs(1000, 1, 1000000000000000))
