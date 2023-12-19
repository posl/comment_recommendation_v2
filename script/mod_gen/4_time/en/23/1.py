def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    return math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1))

if __name__ == '__main__':
    poorPigs()