class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1==0:
            return 0
        repeatCount=[0]*(len(s2)+1)
        nextIndex=[0]*(len(s2)+1)
        j,count=0,0
        for k in range(n1):
            for i in range(len(s1)):
                if s1[i]==s2[j]:
                    j+=1
                    if j==len(s2):
                        j=0
                        count+=1
            repeatCount[k]=count
            nextIndex[k]=j
            for start in range(k):
                if nextIndex[start]==j:
                    prefixCount=repeatCount[start]
                    patternCount=(repeatCount[k]-repeatCount[start])*((n1-1-start)//(k-start))
                    suffixCount=repeatCount[start+(n1-1-start)%(k-start)]-repeatCount[start]
                    return (prefixCount+patternCount+suffixCount)//n2
        return repeatCount[n1-1]//n2

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))