class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = len(primes)
        primes = sorted(primes)
        index = [0] * i
        next_multiple = primes.copy()
        for j in range(1, n):
            ugly[j] = min(next_multiple)
            for k in range(i):
                if ugly[j] == next_multiple[k]:
                    index[k] += 1
                    next_multiple[k] = ugly[index[k]] * primes[k]
        return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))