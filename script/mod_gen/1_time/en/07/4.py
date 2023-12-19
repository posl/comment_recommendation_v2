def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    count = 1
    while count < n:
        min_val = float('inf')
        min_index = -1
        for j in range(len(primes)):
            if primes[j] * ugly[i[j]] < min_val:
                min_val = primes[j] * ugly[i[j]]
                min_index = j
            elif primes[j] * ugly[i[j]] == min_val:
                i[j] += 1
        if min_val != ugly[count - 1]:
            ugly[count] = min_val
            count += 1
        i[min_index] += 1
    return ugly[n - 1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
