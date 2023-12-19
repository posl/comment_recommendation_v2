def reduce_to_one(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + reduce_to_one(n // 2)
    else:
        return 1 + min(reduce_to_one(n + 1), reduce_to_one(n - 1))
print(reduce_to_one(10))
print(reduce_to_one(15))
print(reduce_to_one(16))
print(reduce_to_one(17))
