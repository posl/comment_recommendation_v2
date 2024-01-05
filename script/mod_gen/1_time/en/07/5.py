def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = 1
    index = [0] * len(primes)
    while i < n:
        minUgly = float('inf')
        for j in range(len(primes)):
            minUgly = min(minUgly, primes[j] * ugly[index[j]])
        for j in range(len(primes)):
            if minUgly == primes[j] * ugly[index[j]]:
                index[j] += 1
        ugly[i] = minUgly
        i += 1
    return ugly[n-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = nthSuperUglyNumber(n, primes)
    print(a)