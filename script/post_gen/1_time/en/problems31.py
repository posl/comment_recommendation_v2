Synthesizing 9/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:        
        if n1 == 0:
            return 0
        s1cnt, index, s2cnt = 0, 0, 0
        # recall 是我们用来找循环节的变量，它是一个哈希映射
        # 我们如何找循环节呢？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
        # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中的第 index 个字符，就有循环节了
        # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次匹配到的位置
        # 它们两个必然是相等的，因为我们是在 s1cnt' == s1cnt 时才进行下一次匹配的
        # 因此我们可以用 recall 记录每次的 (s2cnt, index)，当我们发现新的 (s2cnt, index) 出现时，我们就可以计算出循环节的长度，即 (s1cnt - s1cnt') * (s2cnt - s2cnt')，以及每个循环节包含的 s2 的数量
        # 我们用 remain = n1 - s1cnt' 表示还剩下多少个 s1，注意 s1 是可以重复使用的，我们要尽可能先用完之前的 s1
        # 注意这里一定要从 s1cnt' 开始遍历，因为 s2cnt' < s2cnt 时我们是不能算匹配了的
        recall = dict()
        while True:
            # 我们多遍历一个 s1，看看能不能找到循环节
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len

=======
Suggestion 3

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        
        #s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
        #s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaaaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaaaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaaaaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaa", n2 = 1
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaa", n2 = 2
        #s1 = "aaa", n1 = 3, s2 = "aaaaaaaaaa", n

=======
Suggestion 4

def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        count1 = 0
        count2 = 0
        i = 0
        j = 0
        while count1 < n1:
            if s1[i] == s2[j]:
                j += 1
                if j == len(s2):
                    j = 0
                    count2 += 1
            i += 1
            if i == len(s1):
                i = 0
                count1 += 1
        return count2 // n2

=======
Suggestion 5

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 1. brute force
        # 2. dp
        # 3. greedy
        # 4. math
        # 5. dfs
        # 6. bfs
        # 7. two pointers
        # 8. sliding window
        # 9. monotonic stack
        # 10. binary search
        # 11. recursion
        # 12. tree
        # 13. graph
        # 14. trie
        # 15. union find
        # 16. sort
        # 17. bucket sort
        # 18. heap
        # 19. math
        # 20. bit manipulation
        # 21. string
        # 22. array
        # 23. linked list
        # 24. stack
        # 25. queue
        # 26. hash table
        # 27. design
        # 28. greedy
        # 29. binary search
        # 30. recursion
        # 31. tree
        # 32. graph
        # 33. trie
        # 34. union find
        # 35. sort
        # 36. bucket sort
        # 37. heap
        # 38. math
        # 39. bit manipulation
        # 40. string
        # 41. array
        # 42. linked list
        # 43. stack
        # 44. queue
        # 45. hash table
        # 46. design
        # 47. greedy
        # 48. binary search
        # 49. recursion
        # 50. tree
        # 51. graph
        # 52. trie
        # 53. union find
        # 54. sort
        # 55. bucket sort
        # 56. heap
        # 57. math
        # 58. bit manipulation
        # 59. string
        # 60. array
        # 61. linked list
        # 62. stack
        # 63. queue
        # 64. hash table
        # 65. design
        # 66. greedy
        # 67. binary search
        # 68. recursion

=======
Suggestion 6

def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0: return 0
        s1cnt, index, s2cnt = 0, 0, 0
        # recall 是我们用来找循环节的变量，它是一个哈希映射
        # 我们如何找循环节？假设我们遍历了若干个 s1，此时匹配到了某一个 s2 的第 i 个字符
        # 如果我们之前遍历了若干个 s1，匹配到的正是第 i 个字符，那么就有循环节了
        # 我们用 (last_s1_cnt, last_s2_cnt) 表示这个循环节出现之前的 s1 和 s2 的数目
        # 从而我们可以用 (last_s1_cnt, last_s2_cnt) 推出当前遍历的 s1 和 s2 的数目
        # 有了当前的 s1 和 s2 的数目，我们就可以算出匹配了多少个 s2，然后更新 res 即可
        recall = dict()
        while True:
            # 我们多遍历一个 s1，看看能不能找到循环节
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt, index = s2cnt + 1, 0
            # 还没有找到循环节，所有的 s1 就用完了
            if s1cnt == n1:
                return s2cnt // n2
            # 出现了之前的 index，表示找到了循环节
            if index in recall:
                last_s1cnt, last_s2cnt = recall[index]
                # 前 s1cnt' 个 s1 包含了 s1cnt - s1cnt' 个循环节
                circle_s1cnt = s1cnt - last_s1cnt
                circle_s2cnt = s2cnt - last_s2cnt
                # 把

=======
Suggestion 7

def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        idx = 0
        cnt = 0
        for i in range(n1):
            for j in range(len(s1)):
                if s1[j] == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        cnt += 1
                        idx = 0
        return cnt // n2

=======
Suggestion 8

def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:        
        rep1, rep2, idx = 0, 0, 0
        while rep1 < n1:
            for c in s1:
                if c == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        idx = 0
                        rep2 += 1
            rep1 += 1
        return rep2 // n2

=======
Suggestion 9

def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        # edge cases
        if n1 == 0:
            return 0
        if n2 == 0 or len(s2) == 0:
            return 1

        # initialize
        repeatCount = [0] * (len(s2) + 1)
        nextIndex = [0] * (len(s2) + 1)
        j, count = 0, 0

        # loop for s1
        for k in range(1, n1 + 1):
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1

            repeatCount[k] = count
            nextIndex[k] = j

            # check repeat pattern
            for start in range(k):
                if nextIndex[start] == j:
                    prefixCount = repeatCount[start]
                    patternCount = (repeatCount[k] - repeatCount[start]) * ((n1 - start) // (k - start))
                    suffixCount = repeatCount[start + (n1 - start) % (k - start)] - repeatCount[start]
                    return (prefixCount + patternCount + suffixCount) // n2

        return repeatCount[n1] // n2
