Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    return int(math.ceil(math.log(buckets, minutesToTest//minutesToDie+1)))

=======
Suggestion 2

def poorPigs(buckets,minutesToDie,minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

buckets = 4
minutesToDie = 15
minutesToTest = 15
print(poorPigs(buckets,minutesToDie,minutesToTest))

=======
Suggestion 3

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    pigs = 0
    while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

print(poorPigs(1000, 15, 60))
print(poorPigs(1000, 15, 45))
print(poorPigs(1000, 15, 30))
print(poorPigs(1000, 15, 15))
print(poorPigs(1000, 15, 5))
print(poorPigs(1000, 15, 1))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(4, 15, 60))
print(poorPigs(1000, 60, 15))
print(poorPigs(1000, 45, 15))
print(poorPigs(1000, 30, 15))
print(poorPigs(1000, 15, 15))
print(poorPigs(1000, 5, 15))
print(poorPigs(1000, 1, 15))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 30, 15))
print(poorPigs(4, 60, 15))

=======
Suggestion 4

def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie+1))

print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1000, 15, 60))
print(poorPigs(1000, 15, 120))
print(poorPigs(1000, 15, 240))
print(poorPigs(1000, 15, 480))
print(poorPigs(1000, 15, 960))
print(poorPigs(1000, 15, 1440))
print(poorPigs(1000, 15, 2880))
print(poorPigs(1000, 15, 5760))
print(poorPigs(1000, 15, 11520))
print(poorPigs(1000, 15, 23040))
print(poorPigs(1000, 15, 46080))
print(poorPigs(1000, 15, 92160))
print(poorPigs(1000, 15, 184320))
print(poorPigs(1000, 15, 368640))
print(poorPigs(1000, 15, 737280))
print(poorPigs(1000, 15, 1474560))
print(poorPigs(1000, 15, 2949120))
print(poorPigs(1000, 15, 5898240))
print(poorPigs(1000, 15, 11796480))
print(poorPigs(1000, 15, 23592960))
print(poorPigs(1000, 15, 47185920))
print(poorPigs(1000, 15, 94371840))
print(poorPigs(1000, 15, 188743680))
print(poorPigs(1000, 15, 377487360))
print(poorPigs(1000, 15, 754974720))
print(poorPigs(1000, 15, 1509949440))
print(poorPigs(1000, 15,

=======
Suggestion 5

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

=======
Suggestion 6

def poorPigs(buckets, minutesToDie, minutesToTest):
    if buckets == 1:
        return 0
    if minutesToTest / minutesToDie == 1:
        return buckets - 1
    if minutesToTest / minutesToDie == 2:
        return buckets - 2
    if minutesToTest / minutesToDie == 3:
        return buckets - 3
    if minutesToTest / minutesToDie == 4:
        return buckets - 4
    if minutesToTest / minutesToDie == 5:
        return buckets - 5
    if minutesToTest / minutesToDie == 6:
        return buckets - 6
    if minutesToTest / minutesToDie == 7:
        return buckets - 7
    if minutesToTest / minutesToDie == 8:
        return buckets - 8
    if minutesToTest / minutesToDie == 9:
        return buckets - 9
    if minutesToTest / minutesToDie == 10:
        return buckets - 10
    if minutesToTest / minutesToDie == 11:
        return buckets - 11
    if minutesToTest / minutesToDie == 12:
        return buckets - 12
    if minutesToTest / minutesToDie == 13:
        return buckets - 13
    if minutesToTest / minutesToDie == 14:
        return buckets - 14
    if minutesToTest / minutesToDie == 15:
        return buckets - 15
    if minutesToTest / minutesToDie == 16:
        return buckets - 16
    if minutesToTest / minutesToDie == 17:
        return buckets - 17
    if minutesToTest / minutesToDie == 18:
        return buckets - 18
    if minutesToTest / minutesToDie == 19:
        return buckets - 19
    if minutesToTest / minutesToDie == 20:
        return buckets - 20
    if minutesToTest / minutesToDie == 21:
        return buckets - 21
    if minutesToTest / minutesToDie == 22:
        return buckets - 22
    if minutesToTest / minutesToDie == 23:
        return buckets - 23
    if minutesToTest / minutesToDie == 24:

=======
Suggestion 7

def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1))

print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(1000, 15, 60))

=======
Suggestion 8

def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie+1))
