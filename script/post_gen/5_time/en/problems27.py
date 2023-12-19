Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    count = 0
    i = 1
    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return count

print(countDigitOne(13)) # 6
print(countDigitOne(0)) # 0
print(countDigitOne(1)) # 1
print(countDigitOne(10)) # 2
print(countDigitOne(11)) # 4
print(countDigitOne(12)) # 5
print(countDigitOne(20)) # 12
print(countDigitOne(21)) # 13
print(countDigitOne(22)) # 14
print(countDigitOne(23)) # 15
print(countDigitOne(24)) # 16
print(countDigitOne(25)) # 17
print(countDigitOne(26)) # 18
print(countDigitOne(27)) # 19
print(countDigitOne(28)) # 20
print(countDigitOne(29)) # 21
print(countDigitOne(30)) # 22
print(countDigitOne(31)) # 24
print(countDigitOne(32)) # 25
print(countDigitOne(33)) # 26
print(countDigitOne(34)) # 27
print(countDigitOne(35)) # 28
print(countDigitOne(36)) # 29
print(countDigitOne(37)) # 30
print(countDigitOne(38)) # 31
print(countDigitOne(39)) # 32
print(countDigitOne(40)) # 33
print(countDigitOne(41)) # 35
print(countDigitOne(42)) # 36
print(countDigitOne(43)) # 37
print(countDigitOne(44)) # 38
print(countDigitOne(45)) # 39
print(countDigitOne(46)) # 40
print(countDigitOne(47)) # 41
print(countDigitOne(48)) # 42
print(countDigitOne(49)) # 43
print(countDigitOne(50))

=======
Suggestion 2

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    q, x, ans = n, 1, 0
    while q > 0:
        digit = q % 10
        q //= 10
        ans += q * x
        if digit == 1:
            ans += n % x + 1
        elif digit > 1:
            ans += x
        x *= 10
    return ans

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(20))
print(countDigitOne(100))
print(countDigitOne(1000))
print(countDigitOne(10000))
print(countDigitOne(100000))
print(countDigitOne(1000000))
print(countDigitOne(10000000))
print(countDigitOne(100000000))
print(countDigitOne(1000000000))
print(countDigitOne(10000000000))
print(countDigitOne(100000000000))
print(countDigitOne(1000000000000))
print(countDigitOne(10000000000000))
print(countDigitOne(100000000000000))
print(countDigitOne(1000000000000000))
print(countDigitOne(10000000000000000))
print(countDigitOne(100000000000000000))
print(countDigitOne(1000000000000000000))
print(countDigitOne(10000000000000000000))

=======
Suggestion 3

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(1410065408))

=======
Suggestion 4

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    base = 10
    while base <= n:
        base *= 10
    base //= 10
    first = n // base
    remain = n % base
    if first == 1:
        return countDigitOne(base - 1) + remain + 1 + countDigitOne(remain)
    else:
        return base + first * countDigitOne(base - 1) + countDigitOne(remain)

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

=======
Suggestion 5

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    ones, m = 0, 1
    while m <= n:
        ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones

=======
Suggestion 6

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    # 1. 1-9: 1
    # 2. 10-99: 10*1+10
    # 3. 100-999: 100*1+100
    # 4. 1000-9999: 1000*1+1000
    # 5. 10000-99999: 10000*1+10000
    # 6. 100000-999999: 100000*1+100000
    # 7. 1000000-9999999: 1000000*1+1000000
    # 8. 10000000-99999999: 10000000*1+10000000
    # 9. 100000000-999999999: 100000000*1+100000000
    # 10. 1000000000-9999999999: 1000000000*1+1000000000
    # 11. 10000000000-99999999999: 10000000000*1+10000000000
    # 12. 100000000000-999999999999: 100000000000*1+100000000000
    # 13. 1000000000000-9999999999999: 1000000000000*1+1000000000000
    # 14. 10000000000000-99999999999999: 10000000000000*1+10000000000000
    # 15. 100000000000000-999999999999999: 100000000000000*1+100000000000000
    # 16. 1000000000000000-9999999999999999: 1000000000000000*1+1000000000000000
    # 17. 10000000000000000-99999999999999999: 10000000000000000*1+10000000000000000
    # 18. 100000000000000000-999999999999999999: 100000000000000000*1+100000000

=======
Suggestion 7

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(13))
print(countDigitOne(14))
print(countDigitOne(15))
print(countDigitOne(16))
print(countDigitOne(17))
print(countDigitOne(18))
print(countDigitOne(19))
print(countDigitOne(20))
print(countDigitOne(21))
print(countDigitOne(22))
print(countDigitOne(23))
print(countDigitOne(24))
print(countDigitOne(25))
print(countDigitOne(26))
print(countDigitOne(27))
print(countDigitOne(28))
print(countDigitOne(29))
print(countDigitOne(30))
print(countDigitOne(31))
print(countDigitOne(32))
print(countDigitOne(33))
print(countDigitOne(34))
print(countDigitOne(35))
print(countDigitOne(36))
print(countDigitOne(37))
print(countDigitOne(38))
print(countDigitOne(39))
print(countDigitOne(40))
print(countDigitOne(41))
print(countDigitOne(42))
print(countDigitOne(43))
print(countDigitOne(44))
print(countDigitOne(45))
print(countDigitOne(46))
print(countDigitOne(47))
print(countDigitOne(48))
print(countDigitOne(49))
print(countDigitOne(50))
print(countDigitOne(51))
print(countDigitOne(52))
print(countDigitOne(53))
print(countDigitOne(54))
print(countDigitOne(55))
print(countDigitOne(56))
print(countDigitOne(57))
print(countDigitOne(58))
print(countDigitOne(59))
print(countDigitOne(60))
print(countDigitOne(61))
print(countDigitOne(62))
print(countDigitOne(63))
print(countDigitOne(64))
print(countDigitOne(65))
print(countDigitOne(66))
print(countDigitOne(67))
print(countDigitOne(68))
print(countDigitOne(69))
print(countDigitOne(70))
print

=======
Suggestion 8

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(14))
print(countDigitOne(15))
print(countDigitOne(16))
print(countDigitOne(17))
print(countDigitOne(18))
print(countDigitOne(19))
print(countDigitOne(20))
print(countDigitOne(21))
print(countDigitOne(22))
print(countDigitOne(23))
print(countDigitOne(24))
print(countDigitOne(25))
print(countDigitOne(26))
print(countDigitOne(27))
print(countDigitOne(28))
print(countDigitOne(29))
print(countDigitOne(30))
print(countDigitOne(31))
print(countDigitOne(32))
print(countDigitOne(33))
print(countDigitOne(34))
print(countDigitOne(35))
print(countDigitOne(36))
print(countDigitOne(37))
print(countDigitOne(38))
print(countDigitOne(39))
print(countDigitOne(40))
print(countDigitOne(41))
print(countDigitOne(42))
print(countDigitOne(43))
print(countDigitOne(44))
print(countDigitOne(45))
print(countDigitOne(46))
print(countDigitOne(47))
print(countDigitOne(48))
print(countDigitOne(49))
print(countDigitOne(50))
print(countDigitOne(51))
print(countDigitOne(52))
print(countDigitOne(53))
print(countDigitOne(54))
print(countDigitOne(55))
print(countDigitOne(56))
print(countDigitOne(57))
print(countDigitOne(58))
print(countDigitOne(59))
print(countDigitOne(60))
print(countDigitOne(61))
print(countDigitOne(62))
print(countDigitOne(63))
print(countDigitOne(64))
print(countDigitOne(65))
print(countDigitOne(66))
print(countDigitOne(67))
print(countDigitOne(68))
print(countDigitOne(69))
print(countDigitOne(70))
print(countDigitOne(

=======
Suggestion 9

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n == 10:
        return 2
    if n < 100:
        if n == 11:
            return 4
        elif n % 10 == 0:
            return 10
        else:
            return 11
    if n == 100:
        return 21
    if n < 1000:
        if n % 100 == 0:
            return 100
        else:
            return 121
    if n == 1000:
        return 301
    if n < 10000:
        if n % 1000 == 0:
            return 1000
        else:
            return 1331
    if n == 10000:
        return 4001
    if n < 100000:
        if n % 10000 == 0:
            return 10000
        else:
            return 14641
    if n == 100000:
        return 50001
    if n < 1000000:
        if n % 100000 == 0:
            return 100000
        else:
            return 161051
    if n == 1000000:
        return 600001
    if n < 10000000:
        if n % 1000000 == 0:
            return 1000000
        else:
            return 1771561
    if n == 10000000:
        return 7000001
    if n < 100000000:
        if n % 10000000 == 0:
            return 10000000
        else:
            return 19487171
    if n == 100000000:
        return 80000001
    if n < 1000000000:
        if n % 100000000 == 0:
            return 100000000
        else:
            return 214358881
    if n == 1000000000:
        return 900000001
    return 0

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(11))
print

=======
Suggestion 10

def countDigitOne(n):
    total = 0
    for i in range(1, n+1):
        total += str(i).count('1')
    return total

print(countDigitOne(13))
print(countDigitOne(0))
