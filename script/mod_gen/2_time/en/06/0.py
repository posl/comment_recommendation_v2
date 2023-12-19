def nthUglyNumber(n):
    ugly = [0] * n # To store ugly numbers
    ugly[0] = 1
    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 =i5 = 0
    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):
        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[-1]
print(nthUglyNumber(10)) #12
print(nthUglyNumber(1)) #1
print(nthUglyNumber(2)) #2
print(nthUglyNumber(3)) #3
print(nthUglyNumber(4)) #4
print(nthUglyNumber(5)) #5
print(nthUglyNumber(6)) #6
print(nthUglyNumber(7)) #8
print(nthUglyNumber(8)) #9
print(nthUglyNumber(9)) #10
print(nthUglyNumber(11)) #15
print(nthUglyNumber(12)) #16
print(nthUglyNumber(13)) #18
print(nthUglyNumber(14)) #20
print(nthUglyNumber(15)) #24
print(nthUglyNumber(16)) #25
print(nthUglyNumber(17)) #27
print(nthUglyNumber(18)) #30
print(nthUgly

if __name__ == '__main__':
    nthUglyNumber()