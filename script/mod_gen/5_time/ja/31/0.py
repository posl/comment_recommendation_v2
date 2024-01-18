class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        str1 = [s1, n1]
        str2 = [s2, n2]
        print(str1)
        print(str2)
        return 0

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))