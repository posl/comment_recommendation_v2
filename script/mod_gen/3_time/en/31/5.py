def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    # The main idea is to find the loop and then find the
    # number of times the loop repeats itself.
    # If the loop starts at s1[i] and s2[j], then the loop repeats
    # every time s1[i] == s1[i + 1] and s2[j] == s2[j + 1]
    # We can use this to find the loop and then find the number of times
    # the loop repeats itself.
    i = 0
    j = 0
    count1 = 0
    count2 = 0
    while count1 < n1:
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                count2 += 1
                j = 0
        i += 1
        if i == len(s1):
            count1 += 1
            i = 0
    return count2 // n2
s1 = "acb"
n1 = 4
s2 = "ab"
n2 = 2
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "acb"
n1 = 1
s2 = "acb"
n2 = 1
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "aaa"
n1 = 3
s2 = "aa"
n2 = 1
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "baba"
n1 = 11
s2 = "baab"
n2 = 1
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "bacaba"
n1 = 3
s2 = "abacab"
n2 = 1
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "aaa"
n1 = 1000000
s2 = "a"
n2 = 1000000
print(getMaxRepetitions(s1, n1, s2, n2))
s1 = "aaa

if __name__ == '__main__':
    getMaxRepetitions()