Synthesizing 10/10 solutions

=======
Suggestion 1

def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        count += 1
    return count

print(integerReplacement(8))
print(integerReplacement(7))
print(integerReplacement(4))
print(integerReplacement(3))
print(integerReplacement(2))
print(integerReplacement(1))
print(integerReplacement(0))
print(integerReplacement(-1))
print(integerReplacement(-2))
print(integerReplacement(-3))
print(integerReplacement(-4))
print(integerReplacement(-5))
print(integerReplacement(-6))
print(integerReplacement(-7))
print(integerReplacement(-8))
print(integerReplacement(-9))
print(integerReplacement(-10))
print(integerReplacement(-11))
print(integerReplacement(-12))
print(integerReplacement(-13))
print(integerReplacement(-14))
print(integerReplacement(-15))
print(integerReplacement(-16))
print(integerReplacement(-17))
print(integerReplacement(-18))
print(integerReplacement(-19))
print(integerReplacement(-20))
print(integerReplacement(-21))
print(integerReplacement(-22))
print(integerReplacement(-23))
print(integerReplacement(-24))
print(integerReplacement(-25))
print(integerReplacement(-26))
print(integerReplacement(-27))
print(integerReplacement(-28))
print(integerReplacement(-29))
print(integerReplacement(-30))
print(integerReplacement(-31))
print(integerReplacement(-32))
print(integerReplacement(-33))
print(integerReplacement(-34))
print(integerReplacement(-35))
print(integerReplacement(-36))
print(integerReplacement(-37))
print(integerReplacement(-38))
print(integerReplacement(-39))
print(integerReplacement(-40))
print(integerReplacement(-41))
print(integerReplacement(-42))
print(integerReplacement(-43))
print(integerReplacement(-44))
print(integerReplacement(-45))
print(integerReplacement(-46))
print(integerReplacement(-47))
print(integerReplacement(-48))
print(integerReplacement(-49))
print(integerReplacement(-50))
print(integerReplacement(-51))
print(integerReplacement(-52))
print(integerReplacement(-53))
print(integerReplacement(-54))
print(integerReplacement(-55))
print(integerReplacement(-56))
print(integerReplacement(-57))
print(integerReplacement(-58))
print(integerReplacement(-59))
print(integerReplacement(-60))
print(integerReplacement(-61))

=======
Suggestion 2

def solution(num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            if num == 3:
                num = num - 1
            else:
                if (num + 1) % 4 == 0:
                    num = num + 1
                else:
                    num = num - 1
        count += 1
    return count

print(solution(8))
print(solution(7))
print(solution(4))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(5))
print(solution(6))
print(solution(9))
print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
print(solution(14))
print(solution(15))
print(solution(16))
print(solution(17))
print(solution(18))
print(solution(19))
print(solution(20))
print(solution(21))
print(solution(22))
print(solution(23))
print(solution(24))
print(solution(25))
print(solution(26))
print(solution(27))
print(solution(28))
print(solution(29))
print(solution(30))
print(solution(31))
print(solution(32))
print(solution(33))
print(solution(34))
print(solution(35))
print(solution(36))
print(solution(37))
print(solution(38))
print(solution(39))
print(solution(40))
print(solution(41))
print(solution(42))
print(solution(43))
print(solution(44))
print(solution(45))
print(solution(46))
print(solution(47))
print(solution(48))
print(solution(49))
print(solution(50))
print(solution(51))
print(solution(52))
print(solution(53))
print(solution(54))
print(solution(55))
print(solution(56))
print(solution(57))
print(solution(58))
print(solution(59))
print(solution(60))
print(solution(61))
print(solution(62))
print(solution(63))
print(solution(64))
print(solution(65))
print(solution(66))
print(solution(67))
print(solution(68))
print(solution(69))
print(solution(70))
print(solution(71))
print(solution(72))
print(solution(73))
print(solution(74))
print(solution(75))
print(solution(76))
print(solution(77

=======
Suggestion 3

def minOperations(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        count += 1
    return count

=======
Suggestion 4

def minimum_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        steps += 1
    return steps


print(minimum_steps(8))
print(minimum_steps(7))
print(minimum_steps(4))
print(minimum_steps(15))
print(minimum_steps(16))
print(minimum_steps(17))
print(minimum_steps(18))
print(minimum_steps(19))
print(minimum_steps(20))
print(minimum_steps(21))
print(minimum_steps(22))
print(minimum_steps(23))
print(minimum_steps(24))
print(minimum_steps(25))
print(minimum_steps(26))
print(minimum_steps(27))
print(minimum_steps(28))
print(minimum_steps(29))
print(minimum_steps(30))
print(minimum_steps(31))
print(minimum_steps(32))
print(minimum_steps(33))
print(minimum_steps(34))
print(minimum_steps(35))
print(minimum_steps(36))
print(minimum_steps(37))
print(minimum_steps(38))
print(minimum_steps(39))
print(minimum_steps(40))
print(minimum_steps(41))
print(minimum_steps(42))
print(minimum_steps(43))
print(minimum_steps(44))
print(minimum_steps(45))
print(minimum_steps(46))
print(minimum_steps(47))
print(minimum_steps(48))
print(minimum_steps(49))
print(minimum_steps(50))
print(minimum_steps(51))
print(minimum_steps(52))
print(minimum_steps(53))
print(minimum_steps(54))
print(minimum_steps(55))
print(minimum_steps(56))
print(minimum_steps(57))
print(minimum_steps(58))
print(minimum_steps(59))
print(minimum_steps(60))
print(minimum_steps(61))
print(minimum_steps(62))
print(minimum_steps(63))
print(minimum_steps(64))
print(minimum_steps(65))
print(minimum_steps(66))
print(minimum_steps(67))
print(minimum_steps(68))
print(minimum_steps(69))
print(minimum_steps(70))
print(minimum_steps(71))
print(minimum_steps(72))
print(minimum_steps(73))
print(minimum_steps(74))
print(minimum

=======
Suggestion 5

def problem13(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            if (n + 1) % 4 == 0 and n != 3:
                n = n + 1
            else:
                n = n - 1
        count += 1
    return count

print(problem13(8))
print(problem13(7))
print(problem13(4))

=======
Suggestion 6

def numberOfSteps(n):
    """
    :type num: int
    :rtype: int
    """
    steps = 0
    while n > 0:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        steps += 1
    return steps

=======
Suggestion 7

def numberOfSteps(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = n - 1
            count += 1
    return count

print(numberOfSteps(14))

=======
Suggestion 8

def reduceToOne(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
        count += 1
    return count

print(reduceToOne(8))
print(reduceToOne(7))
print(reduceToOne(4))

=======
Suggestion 9

def minOperations(n: int) -> int:
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            count += 1
        elif n % 2 != 0:
            n = n - 1
            count += 1
    return count

=======
Suggestion 10

def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        elif n == 3 or n % 4 == 1:
            n -= 1
            count += 1
        else:
            n += 1
            count += 1
    return count

print(integerReplacement(8))
print(integerReplacement(7))
print(integerReplacement(4))
print(integerReplacement(15))
print(integerReplacement(100000000))
