def nthSuperUglyNumber(n, primes):
    ugly = [1]
    pointers = [0] * len(primes)
    while n > 1:
        candidates = [ugly[pointers[i]] * primes[i] for i in range(len(primes))]
        nextUgly = min(candidates)
        ugly.append(nextUgly)
        for i in range(len(primes)):
            if nextUgly == candidates[i]:
                pointers[i] += 1
        n -= 1
    return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = nthSuperUglyNumber(n, primes)
    print(a)