def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1))
print(poorPigs(1000, 15, 60))
