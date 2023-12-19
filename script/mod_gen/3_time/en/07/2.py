def superUglyNumber(n, primes):
    ugly = [1]
    pri = {i:0 for i in primes}
    while len(ugly) < n:
        cand = min([ugly[pri[i]]*i for i in primes])
        ugly.append(cand)
        for i in primes:
            if cand == ugly[pri[i]]*i:
                pri[i] +=1
    return ugly[-1]
print(superUglyNumber(12, [2,7,13,19]))
print(superUglyNumber(1, [2,3,5]))
print(superUglyNumber(100000, [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]))
