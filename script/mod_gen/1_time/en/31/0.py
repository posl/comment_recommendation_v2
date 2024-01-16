class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
        # s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
        # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1
        # s1 = "aaa", n1 = 3, s2 = "aa", n2 = 2
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 1
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 2
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 3
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 4
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 5
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 6
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 7
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 8
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 9
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 10
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 11
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 12
        # s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 13
        # s1 = "bacaba", n1 = 3, s2 =
