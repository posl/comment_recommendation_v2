def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    # 1. find the minimum number of pigs
    # 2. the minimum number of pigs is the number of digits of buckets in the minutesToTest base
    # 3. the minimum number of pigs is the number of digits of buckets in the minutesToTest base
    return math.ceil(math.log(buckets, minutesToTest/minutesToDie+1))

if __name__ == '__main__':
    poorPigs()