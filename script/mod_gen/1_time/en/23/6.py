def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    return int(math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1)))

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = poorPigs(buckets, minutesToDie, minutesToTest)
    print(a)