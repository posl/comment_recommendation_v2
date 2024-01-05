def nthSuperUglyNumber(n, primes):
    ugly = [1]
    # i2, i3, i5 will indicate the indices for the current ugly number multiplied by 2, 3, 5 respectively
    i2, i3, i5 = 0, 0, 0
    # c2, c3, c5 will indicate the current ugly number multiplied by 2, 3, 5 respectively
    c2, c3, c5 = 2, 3, 5
    for i in range(1, n):
        # choose the next ugly number as the minimum of c2, c3, c5
        ugly.append(min(c2, c3, c5))
        # increment the index for the chosen ugly number
        if ugly[i] == c2:
            i2 += 1
            c2 = ugly[i2] * 2
        if ugly[i] == c3:
            i3 += 1
            c3 = ugly[i3] * 3
        if ugly[i] == c5:
            i5 += 1
            c5 = ugly[i5] * 5
    return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = nthSuperUglyNumber(n, primes)
    print(a)