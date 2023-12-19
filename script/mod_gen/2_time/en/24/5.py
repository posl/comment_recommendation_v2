def distinctSubseqII(s):
    """
    :type s: str
    :rtype: int
    """
    mod = 10**9 + 7
    dp = [1] * (len(s) + 1)
    last = {}
    for i, c in enumerate(s):
        dp[i + 1] = dp[i] * 2 % mod
        if c in last:
            dp[i + 1] -= dp[last[c]]
        last[c] = i
    return (dp[-1] - 1) % mod
print(distinctSubseqII("rabbbit"))
print(distinctSubseqII("babgbag"))
print(distinctSubseqII("ab"))
print(distinctSubseqII("abc"))
print(distinctSubseqII("aba"))
print(distinctSubseqII("aaa"))
print(distinctSubseqII("aaaa"))
print(distinctSubseqII("aaaaa"))
print(distinctSubseqII("aaaaaa"))
print(distinctSubseqII("aaaaaaa"))
print(distinctSubseqII("aaaaaaaa"))
print(distinctSubseqII("aaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinctSubseqII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(distinct

if __name__ == '__main__':
    distinctSubseqII()