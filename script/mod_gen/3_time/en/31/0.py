class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:        
        if n1 == 0:
            return 0
        repeatCount, index, nextIndex = 0, 0, 0
        recall = dict()
        while True:
            repeatCount += 1
            for i in range(len(s1)):
                if s1[i] == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        n2 -= 1
            if n2 == 0:
                return repeatCount // n1
            if index in recall:
                prevRepeatCount, prevIndex = recall[index]
                interval = repeatCount - prevRepeatCount
                repeatCount = prevRepeatCount + (n1 - prevRepeatCount) // interval * interval
                n2 -= (prevIndex - index) * ((n1 - prevRepeatCount) // interval)
            else:
                recall[index] = (repeatCount, index)
        return repeatCount // n1

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))