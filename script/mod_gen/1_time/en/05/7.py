def findSubstringInWraproundString(s):
    """
    :type p: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    dp = [0]*26
    dp[ord(s[0]) - ord('a')] = 1
    count = 1
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
            count += 1
        else:
            count = 1
        dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
    return sum(dp)
    
s1 = "a"
s2 = "cac"
s3 = "zab"
s4 = "zaba"
s5 = "zabca"
s6 = "zabcd"
s7 = "zabcdef"
s8 = "zabcdefg"
s9 = "zabcdefgh"
s10 = "zabcdefghi"
s11 = "zabcdefghij"
s12 = "zabcdefghijk"
s13 = "zabcdefghijkl"
s14 = "zabcdefghijklm"
s15 = "zabcdefghijklmn"
s16 = "zabcdefghijklmno"
s17 = "zabcdefghijklmnop"
s18 = "zabcdefghijklmnopq"
s19 = "zabcdefghijklmnopqr"
s20 = "zabcdefghijklmnopqrs"
s21 = "zabcdefghijklmnopqrst"
s22 = "zabcdefghijklmnopqrstu"
s23 = "zabcdefghijklmnopqrstuv"
s24 = "zabcdefghijklmnopqrstuvw"
s25 = "zabcdefghijklmnopqrstuvwx"
s26 = "zabcdefghijklmnopqrstuvwxy"
s27 = "zabcdefghijklmnopqrstuvwxyz"
s28 = "zabcdefghijklmnopqrstuvwxyzab"
s29 = "zabcdefghijklmnopqrstuvwxyzabc"
s30 = "zabcdefghijklmnopqrstuvwxyzabcd"
s31 = "zabcdefghijklmnopqrstuvwxyzabcde"
s32 = "zabcdefghijklmnopqrstuvwxyzabcdef"
s33 = "zabcdefghijklmnopqrstuvwxyzabcdefg"
s34 = "zabcdefghijklmnopqrstuvwxyzabcdefgh"
s35 = "zabcdefghijklmnopqrstuvwxyzabcdefghi"
s36 = "zabcdefghijklmnopqrstuvwxyzabcdefghij"
s37 = "zabcdefghijklmnopqrstuvwxyzabcdefghijk"
s38 = "zabcdefghijklmnopqrstuvwxyzabcdefghijkl"
s39 = "zabcdefghijklmnopqrstuvwxyzabcdefghijklm"
s40 = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmn"
s41 = "zabcdefghijklmnopqrstuvwxyzabcdefghijklmno"
s42 = "

if __name__ == '__main__':
    s = input()
    a = findSubstringInWraproundString(s)
    print(a)