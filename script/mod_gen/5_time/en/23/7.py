def poorPigs(buckets, minutesToDie, minutesToTest):
    import math
    return math.ceil(math.log(buckets, minutesToTest//minutesToDie+1))

if __name__ == '__main__':
    poorPigs()