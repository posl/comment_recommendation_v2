def count_digit_one(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n == 10:
        return 2
    if n == 11:
        return 4
    if n < 20:
        return 4 + count_digit_one(n - 10)
    if n < 100:
        return 10 + 2 * count_digit_one(n - 10)
    if n < 1000:
        return 300 + 2 * count_digit_one(n - 100)
    if n < 2000:
        return 400 + 3 * count_digit_one(n - 1000)
    if n < 10000:
        return 4000 + 4 * count_digit_one(n - 1000)
    if n < 20000:
        return 5000 + 5 * count_digit_one(n - 10000)
    if n < 100000:
        return 50000 + 5 * count_digit_one(n - 10000)
    if n < 200000:
        return 60000 + 6 * count_digit_one(n - 100000)
    if n < 1000000:
        return 600000 + 6 * count_digit_one(n - 100000)
    if n < 2000000:
        return 700000 + 7 * count_digit_one(n - 1000000)
    if n < 10000000:
        return 7000000 + 7 * count_digit_one(n - 1000000)
    if n < 20000000:
        return 8000000 + 8 * count_digit_one(n - 10000000)
    if n < 100000000:
        return 80000000 + 8 * count_digit_one(n - 10000000)
    if n < 200000000:
        return 90000000 + 9 * count_digit_one(n - 100000000)
    if n < 1000000000:
        return 900000000 + 9 * count_digit_one(n - 100000000)
    if n < 2000000000:
        return 1000000000 + 10 * count_digit_one(n - 1000000000)

if __name__ == '__main__':
    count_digit_one()