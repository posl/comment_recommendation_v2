def poorPigs(buckets, minutesToDie, minutesToTest):
    # https://leetcode.com/problems/poor-pigs/discuss/94273/Solution-with-detailed-explanation
    # the idea is to use the base of the number of buckets, the number of minutes to die and the number of minutes to test to calculate the number of pigs
    # in the example 1, buckets = 4, minutesToDie = 15, minutesToTest = 15
    # the number of pigs is 2 because 4 = (1 + 1) ^ 2, where 1 + 1 is the number of minutes to die + 1
    # in the example 2, buckets = 4, minutesToDie = 15, minutesToTest = 30
    # the number of pigs is 2 because 4 = (1 + 1) ^ 2, where 1 + 1 is the number of minutes to die + 1
    # in the example 3, buckets = 1000, minutesToDie = 12, minutesToTest = 60
    # the number of pigs is 5 because 1000 = (4 + 1) ^ 5, where 4 + 1 is the number of minutes to die + 1
    import math
    return math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1))

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = poorPigs(buckets, minutesToDie, minutesToTest)
    print(a)