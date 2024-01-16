class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next_ugly = min(ugly[pointers[i]] * primes[i] for i in range(len(primes)))
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if ugly[pointers[i]] * primes[i] == next_ugly:
                    pointers[i] += 1
        return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))