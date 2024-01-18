class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        cnt = 0
        i = 0
        j = 0
        while i < n1:
            if s1[i % len(s1)] == s2[j % len(s2)]:
                j += 1
            i += 1
            if j % len(s2) == 0:
                cnt += 1
        return cnt // n2

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))