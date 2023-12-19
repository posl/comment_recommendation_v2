def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    import math
    return math.ceil(math.log(buckets, (minutesToTest // minutesToDie) + 1))
print(poorPigs(1000, 15, 60))
print(poorPigs(4, 15, 15))
print(poorPigs(4, 15, 30))
print(poorPigs(9, 15, 60))
print(poorPigs(9, 15, 90))
print(poorPigs(9, 15, 120))
print(poorPigs(9, 15, 150))
print(poorPigs(9, 15, 180))
print(poorPigs(9, 15, 210))
print(poorPigs(9, 15, 240))
print(poorPigs(9, 15, 270))
print(poorPigs(9, 15, 300))
print(poorPigs(9, 15, 330))
print(poorPigs(9, 15, 360))
print(poorPigs(9, 15, 390))
print(poorPigs(9, 15, 420))
print(poorPigs(9, 15, 450))
print(poorPigs(9, 15, 480))
print(poorPigs(9, 15, 510))
print(poorPigs(9, 15, 540))
print(poorPigs(9, 15, 570))
print(poorPigs(9, 15, 600))
print(poorPigs(9, 15, 630))
print(poorPigs(9, 15, 660))
print(poorPigs(9, 15, 690))
print(poorPigs(9, 15, 720))
print(poorPigs(9, 15, 750))
print(poorPigs(9, 15, 780))
print(poorPigs(9, 15, 810))
print(poorPigs(9, 15, 840))
print(poorP

if __name__ == '__main__':
    poorPigs()