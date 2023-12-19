def nthUglyNumber(n):
    # 1 is always an ugly number
    ugly = [1]
    # keep track of the last index of each ugly number
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        # get the next ugly number by multiplying the minimum of the ugly numbers at the current indices
        # by the corresponding prime
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        # check if the ugly number at the current index is a multiple of the corresponding prime
        # if so, increment the index
        if ugly[-1] == ugly[i2] * 2:
            i2 += 1
        if ugly[-1] == ugly[i3] * 3:
            i3 += 1
        if ugly[-1] == ugly[i5] * 5:
            i5 += 1
        n -= 1
    return ugly[-1]

if __name__ == '__main__':
    nthUglyNumber()