def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets==1:
        return 0
    else:
        return int(math.ceil(math.log(buckets, minutesToTest//minutesToDie+1)))

if __name__ == '__main__':
    poorPigs()