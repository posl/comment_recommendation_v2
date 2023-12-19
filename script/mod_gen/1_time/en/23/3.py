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
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(25, 15, 60))
print("The values above should be 2, 2, and 2.")

if __name__ == '__main__':
    poorPigs()