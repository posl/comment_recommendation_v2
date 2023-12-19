def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets)/math.log(minutesToTest//minutesToDie + 1))
buckets = 4
minutesToDie = 15
minutesToTest = 15
print(poorPigs(buckets, minutesToDie, minutesToTest))
