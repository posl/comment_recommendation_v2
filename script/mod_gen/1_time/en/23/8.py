def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToDie >= minutesToTest:
        return -1
    if buckets == 2:
        return 1
    if minutesToDie == 1:
        return buckets - 1
    if minutesToDie == 2:
        return buckets - 2
    if minutesToDie == 3:
        if minutesToTest == 4:
            return buckets - 2
        elif minutesToTest == 5:
            return buckets - 3
        elif minutesToTest == 6:
            return buckets - 3
        elif minutesToTest == 7:
            return buckets - 3
        elif minutesToTest == 8:
            return buckets - 3
        elif minutesToTest == 9:
            return buckets - 3
        elif minutesToTest == 10:
            return buckets - 3
        elif minutesToTest == 11:
            return buckets - 3
        elif minutesToTest == 12:
            return buckets - 3
        elif minutesToTest == 13:
            return buckets - 3
        elif minutesToTest == 14:
            return buckets - 3
        elif minutesToTest == 15:
            return buckets - 3
        elif minutesToTest == 16:
            return buckets - 3
        elif minutesToTest == 17:
            return buckets - 3
        elif minutesToTest == 18:
            return buckets - 3
        elif minutesToTest == 19:
            return buckets - 3
        elif minutesToTest == 20:
            return buckets - 3
        elif minutesToTest == 21:
            return buckets - 3
        elif minutesToTest == 22:
            return buckets - 3
        elif minutesToTest == 23:
            return buckets - 3
        elif minutesToTest == 24:
            return buckets - 3
        elif minutesToTest == 25:
            return buckets - 3
        elif minutesToTest == 26:
            return buckets - 3
        elif minutes

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    a = poorPigs(buckets, minutesToDie, minutesToTest)
    print(a)