class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        i = 0
        while len(ugly) < n:
            ugly.append(min([ugly[j] * primes[i] for j in range(len(ugly))]))
            i = ugly.index(ugly[-1] / primes[i])
        return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))