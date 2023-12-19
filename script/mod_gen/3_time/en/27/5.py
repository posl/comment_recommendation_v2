def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    if n < 10:
        return 1
    # find the highest digit
    digit = 1
    while digit <= n:
        digit *= 10
    digit //= 10
    # find the number of 1s in the highest digit
    count = 0
    if n // digit == 1:
        count += n % digit + 1
    else:
        count += digit
    # find the number of 1s in the rest digits
    count += (n // digit) * countDigitOne(digit - 1)
    # find the number of 1s in the rest numbers
    count += countDigitOne(n % digit)
    return count

if __name__ == '__main__':
    countDigitOne()