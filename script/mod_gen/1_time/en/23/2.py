def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1000, 15, 60))
print(poorPigs(1000, 15, 15))
print(poorPigs(1, 1, 1))
print("The values above should be 2, 2, 5, 1, and 0.")

if __name__ == '__main__':
    poorPigs()