def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, (minutesToTest // minutesToDie) + 1))
print(poorPigs(1000, 15, 60))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(9, 15, 60))
print(poorPigs(1000, 12, 60))
print(poorPigs(1000, 12, 100))
