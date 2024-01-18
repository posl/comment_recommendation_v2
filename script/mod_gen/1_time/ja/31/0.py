class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s1 = s1*n1
        s2 = s2*n2
        cnt = 0
        j = 0
        for i in range(len(s1)):
            if s1[i] == s2[j]:
                j += 1
            if j == len(s2):
                cnt += 1
                j = 0
        return cnt//n2

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))