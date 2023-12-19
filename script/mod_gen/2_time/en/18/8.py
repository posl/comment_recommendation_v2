def countNumbersWithUniqueDigits(n):
    if n==0:
        return 1
    if n==1:
        return 10
    if n==2:
        return 91
    if n>2:
        ans=91
        for i in range(3,n+1):
            ans+=(9*permutation(9,i-1))
        return ans

if __name__ == '__main__':
    countNumbersWithUniqueDigits()