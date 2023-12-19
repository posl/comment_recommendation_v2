def poorPigs(buckets, minutesToDie, minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
buckets = 1000
minutesToDie = 15
minutesToTest = 60
print(poorPigs(buckets, minutesToDie, minutesToTest))
