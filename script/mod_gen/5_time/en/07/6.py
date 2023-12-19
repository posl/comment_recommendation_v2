def nthSuperUglyNumber(n, primes):
    ugly=[1]
    idx=[0]*len(primes)
    for i in range(n-1):
        ugly.append(min([ugly[idx[j]]*primes[j] for j in range(len(primes))]))
        for j in range(len(primes)):
            if ugly[-1]==ugly[idx[j]]*primes[j]:
                idx[j]+=1
    return ugly[-1]
print(nthSuperUglyNumber(12,[2,7,13,19]))
print(nthSuperUglyNumber(1,[2,3,5]))
