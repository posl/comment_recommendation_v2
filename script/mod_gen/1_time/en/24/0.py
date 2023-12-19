def numDistinct(s,t):
    dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0] = 1
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
print(numDistinct("rabbbit","rabbit"))
print(numDistinct("babgbag","bag"))
print(numDistinct("abcd","abcd"))
print(numDistinct("abcd","abc"))
print(numDistinct("abcd","ab"))
print(numDistinct("abcd","a"))
print(numDistinct("abcd",""))
print(numDistinct("","a"))
print(numDistinct("",""))
print(numDistinct("babgbag","babgbag"))
print(numDistinct("babgbag","babgbagb"))
print(numDistinct("babgbag","babgbagbb"))
print(numDistinct("babgbag","babgbagbbb"))
print(numDistinct("babgbag","babgbagbbbb"))
print(numDistinct("babgbag","babgbagbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbbbb"))
print(numDistinct("babgbag","babgbagbbbbbbbbbbbbbbbbbbb"))
