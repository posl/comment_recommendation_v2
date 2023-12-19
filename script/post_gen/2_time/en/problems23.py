Synthesizing 10/10 solutions

=======
Suggestion 1

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    return int(math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1)))

=======
Suggestion 2

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToTest <= minutesToDie:
        return -1
    if buckets == 2:
        return 1
    if buckets == 3:
        return 1
    if buckets == 4:
        return 2
    if buckets == 5:
        return 2
    if buckets == 6:
        return 2
    if buckets == 7:
        return 2
    if buckets == 8:
        return 3
    if buckets == 9:
        return 3
    if buckets == 10:
        return 3
    if buckets == 11:
        return 3
    if buckets == 12:
        return 3
    if buckets == 13:
        return 3
    if buckets == 14:
        return 3
    if buckets == 15:
        return 3
    if buckets == 16:
        return 4
    if buckets == 17:
        return 4
    if buckets == 18:
        return 4
    if buckets == 19:
        return 4
    if buckets == 20:
        return 4
    if buckets == 21:
        return 4
    if buckets == 22:
        return 4
    if buckets == 23:
        return 4
    if buckets == 24:
        return 4
    if buckets == 25:
        return 4
    if buckets == 26:
        return 4
    if buckets == 27:
        return 4
    if buckets == 28:
        return 4
    if buckets == 29:
        return 4
    if buckets == 30:
        return 4
    if buckets == 31:
        return 4
    if buckets == 32:
        return 5
    if buckets == 33:
        return 5
    if buckets == 34:
        return 5
    if buckets == 35:
        return 5
    if buckets == 36:
        return 5
    if buckets ==

=======
Suggestion 3

def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1))

=======
Suggestion 4

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    pass

print(poorPigs(4, 15, 15))

=======
Suggestion 5

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
    else:
        return int(math.ceil(math.log(buckets, 2)))

=======
Suggestion 6

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if buckets <= minutesToTest / minutesToDie + 1:
        return 1
    if buckets <= (minutesToTest / minutesToDie + 1) ** 2:
        return 2
    if buckets <= (minutesToTest / minutesToDie + 1) ** 3:
        return 3
    if buckets <= (minutesToTest / minutesToDie + 1) ** 4:
        return 4
    if buckets <= (minutesToTest / minutesToDie + 1) ** 5:
        return 5
    if buckets <= (minutesToTest / minutesToDie + 1) ** 6:
        return 6
    if buckets <= (minutesToTest / minutesToDie + 1) ** 7:
        return 7
    if buckets <= (minutesToTest / minutesToDie + 1) ** 8:
        return 8
    if buckets <= (minutesToTest / minutesToDie + 1) ** 9:
        return 9
    if buckets <= (minutesToTest / minutesToDie + 1) ** 10:
        return 10
    if buckets <= (minutesToTest / minutesToDie + 1) ** 11:
        return 11
    if buckets <= (minutesToTest / minutesToDie + 1) ** 12:
        return 12
    if buckets <= (minutesToTest / minutesToDie + 1) ** 13:
        return 13
    if buckets <= (minutesToTest / minutesToDie + 1) ** 14:
        return 14
    if buckets <= (minutesToTest / minutesToDie + 1) ** 15:
        return 15
    if buckets <= (minutesToTest / minutesToDie + 1) ** 16:
        return 16
    if buckets <= (minutesToTest / minutesToDie + 1) ** 17:
        return 17
    if buckets <= (minutesToTest / minutesToDie + 1) ** 18

=======
Suggestion 7

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """

    def get_pigs(buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

    return get_pigs(buckets, minutesToDie, minutesToTest)

print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1000, 15, 60))
print(poorPigs(1000, 15, 100))
print(poorPigs(1000, 15, 120))

=======
Suggestion 8

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    import math
    return int(math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1)))

=======
Suggestion 9

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    if buckets == 1:
        return 0
    if minutesToTest <= minutesToDie:
        return -1
    pigs = 1
    while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

print(poorPigs(4, 15, 15)) #2
print(poorPigs(4, 15, 30)) #2
print(poorPigs(1, 1, 1)) #0
print(poorPigs(1000, 15, 60)) #5
print(poorPigs(1000, 12, 60)) #4
print(poorPigs(1000, 1, 60)) #9
print(poorPigs(1000, 1, 100)) #9
print(poorPigs(1000, 1, 1000)) #9
print(poorPigs(1000, 1, 10000)) #9
print(poorPigs(1000, 1, 100000)) #9
print(poorPigs(1000, 1, 1000000)) #9
print(poorPigs(1000, 1, 10000000)) #9
print(poorPigs(1000, 1, 100000000)) #9
print(poorPigs(1000, 1, 1000000000)) #9
print(poorPigs(1000, 1, 10000000000)) #9
print(poorPigs(1000, 1, 100000000000)) #9
print(poorPigs(1000, 1, 1000000000000)) #9
print(poorPigs(1000, 1, 10000000000000)) #9
print(poorPigs(1000, 1, 100000000000000)) #9
print(poorPigs(1000, 1, 1000000000000000))

=======
Suggestion 10

def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1))

print(poorPigs(1000, 15, 60))
