def nthSuperUglyNumber(n, primes):
    # Time: O(n * k) where k is len(primes)
    # Space: O(n + k)
    ugly_nums = [1]
    prime_idx = [0] * len(primes)
    for _ in range(n-1):
        candidates = [ugly_nums[prime_idx[i]] * primes[i] for i in range(len(primes))]
        min_idx = candidates.index(min(candidates))
        prime_idx[min_idx] += 1
        ugly_nums.append(candidates[min_idx])
    return ugly_nums[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()