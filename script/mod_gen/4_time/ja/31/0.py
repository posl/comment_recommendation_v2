class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        def helper(s1, s2):
            if len(s1) < len(s2):
                return 0
            p1, p2 = 0, 0
            while p1 < len(s1):
                if s1[p1] == s2[p2]:
                    p2 += 1
                if p2 == len(s2):
                    break
                p1 += 1
            if p2 < len(s2):
                return 0
            return 1 + helper(s1[p1 + 1:], s2)
        return helper(s1 * n1, s2 * n2) // n2

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))