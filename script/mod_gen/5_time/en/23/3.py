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
