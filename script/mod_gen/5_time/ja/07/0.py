class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        next = ugly[:]
        while len(ugly) < n:
            for i in primes:
                next.append(ugly[-1]*i)
            ugly.append(min(next))
            next = [ugly[-1]]
        return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))