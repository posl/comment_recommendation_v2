def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    ugly = [0] * n  # To store ugly numbers
    ugly[0] = 1  # 1 is the first ugly number
    i2 = i3 = i5 = 0
    # Indices for 2, 3, 5
    # multiples
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    for l in range(1, n):
        # Choose the min value of all the 3
        # choices of multiples of 2, 3, and 5
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)
        # Increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    # Return ugly[n] value
    return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    a = nthUglyNumber(n)
    print(a)