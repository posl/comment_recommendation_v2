Synthesizing 10/10 solutions

=======
Suggestion 1

def solution(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 4 == 1 or n == 3:
            n -= 1
        else:
            n += 1
        count += 1
    return count

=======
Suggestion 2

def reduceNumber(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = n - 1
            count += 1
    return count

print(reduceNumber(8))
print(reduceNumber(7))
print(reduceNumber(4))

=======
Suggestion 3

def minOperations(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        count += 1
    return count

print(minOperations(8))
print(minOperations(7))
print(minOperations(4))
print(minOperations(123))

=======
Suggestion 4

def reduceTo1(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n + 1
        count = count + 1
    return count

=======
Suggestion 5

def number_of_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            steps += 1
        else:
            n = n - 1
            steps += 1
    return steps

print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))
print(number_of_steps(123))
print(number_of_steps(123456789))
print(number_of_steps(1234567890))
print(number_of_steps(12345678901))
print(number_of_steps(123456789012))
print(number_of_steps(1234567890123))
print(number_of_steps(12345678901234))
print(number_of_steps(123456789012345))
print(number_of_steps(1234567890123456))
print(number_of_steps(12345678901234567))
print(number_of_steps(123456789012345678))
print(number_of_steps(1234567890123456789))
print(number_of_steps(12345678901234567890))
print(number_of_steps(123456789012345678901))
print(number_of_steps(1234567890123456789012))
print(number_of_steps(12345678901234567890123))
print(number_of_steps(123456789012345678901234))
print(number_of_steps(1234567890123456789012345))
print(number_of_steps(12345678901234567890123456))
print(number_of_steps(123456789012345678901234567))
print(number_of_steps(1234567890123456789012345678))
print(number_of_steps(12345678901234567890123456789))
print(number_of_steps(123456789012345678901234567890))
print(number_of_steps(1234567890123456789012345678901))
print(number_of_steps(12345678901234567890123456789012))
print(number_of_steps(123456789012345678901234567890123))
print(number_of_steps(1234567890123456789012345678901234))
print(number_of_steps(12345678901234567890123456789012345))
print(number_of_steps(123456789012345678901234567890123456))
print(number_of_steps(1234567890123456789012345678901234567))
print(number_of

=======
Suggestion 6

def numberOfSteps (num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        count = count + 1
    return count

print(numberOfSteps(8)) #3
print(numberOfSteps(7)) #4
print(numberOfSteps(4)) #2

=======
Suggestion 7

def min_operations(n):
    operations = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            if (n - 1) % 4 == 0 or n == 3:
                n -= 1
            else:
                n += 1
        operations += 1
    return operations

=======
Suggestion 8

def number_of_steps(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = n - 1
            count += 1
    return count

print(number_of_steps(14))
print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))
print(number_of_steps(123))
print(number_of_steps(0))
print(number_of_steps(1))
print(number_of_steps(2))
print(number_of_steps(3))
print(number_of_steps(5))
print(number_of_steps(6))
print(number_of_steps(9))
print(number_of_steps(10))
print(number_of_steps(11))
print(number_of_steps(12))
print(number_of_steps(13))
print(number_of_steps(15))
print(number_of_steps(16))
print(number_of_steps(17))
print(number_of_steps(18))
print(number_of_steps(19))
print(number_of_steps(20))
print(number_of_steps(21))
print(number_of_steps(22))
print(number_of_steps(23))
print(number_of_steps(24))
print(number_of_steps(25))
print(number_of_steps(26))
print(number_of_steps(27))
print(number_of_steps(28))
print(number_of_steps(29))
print(number_of_steps(30))
print(number_of_steps(31))
print(number_of_steps(32))
print(number_of_steps(33))
print(number_of_steps(34))
print(number_of_steps(35))
print(number_of_steps(36))
print(number_of_steps(37))
print(number_of_steps(38))
print(number_of_steps(39))
print(number_of_steps(40))
print(number_of_steps(41))
print(number_of_steps(42))
print(number_of_steps(43))
print(number_of_steps(44))
print(number_of_steps(45))
print(number_of_steps(46))
print(number_of_steps(47))
print(number_of_steps(48))
print(number_of_steps(49))
print(number_of_steps(50))
print(number_of_steps(51))
print(number_of_steps(52))
print(number_of_steps(53))
print(number_of_steps(54))
print(number_of_steps(55))
print(number_of_steps(56))
print(number_of_steps(57))
print(number_of_steps(58))
print(number_of_steps(59))
print(number_of_steps(60))
print(number_of_steps

=======
Suggestion 9

def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        count = count + 1
    return count

print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))

=======
Suggestion 10

def minOperations(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + minOperations(n // 2)
    else:
        return 1 + min(minOperations(n + 1), minOperations(n - 1))
