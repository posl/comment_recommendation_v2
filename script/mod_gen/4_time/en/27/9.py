def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    ones, m = 0, 1
    while m <= n:
        ones += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(100))
print(countDigitOne(1000))
print(countDigitOne(10000))
print(countDigitOne(100000))
print(countDigitOne(1000000))
print(countDigitOne(10000000))
print(countDigitOne(100000000))
print(countDigitOne(1000000000))
# Solution:
# 1. 从最低位开始，每次判断该位数字是否为1，若是则计数加1
# 2. 然后判断该位数字是否为0，若是则计数加上高位数字+1
# 3. 然后判断该位数字是否大于1，若是则计数加上m（m为当前位的位数）
# 4. 然后将m乘以10，继续判断下一位数字
# 5. 直到m大于n
# 6. 返回计数
# Beats: 90.34%
# Runtime: 20ms
# hard

if __name__ == '__main__':
    countDigitOne()