Synthesizing 10/10 solutions

=======
Suggestion 1

def integerReplacement(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
        count += 1
    return count

=======
Suggestion 2

def number_of_steps(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    return count

print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))

=======
Suggestion 3

def numberOfSteps(num):
    step = 0
    while(num > 0):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        step += 1
    return step

print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
print(numberOfSteps(123))
print(numberOfSteps(123456789))
print(numberOfSteps(987654321))
print(numberOfSteps(1234567890))
print(numberOfSteps(12345678901))
print(numberOfSteps(123456789012))
print(numberOfSteps(1234567890123))
print(numberOfSteps(12345678901234))
print(numberOfSteps(123456789012345))
print(numberOfSteps(1234567890123456))
print(numberOfSteps(12345678901234567))
print(numberOfSteps(123456789012345678))
print(numberOfSteps(1234567890123456789))
print(numberOfSteps(12345678901234567890))
print(numberOfSteps(123456789012345678901))
print(numberOfSteps(1234567890123456789012))
print(numberOfSteps(12345678901234567890123))
print(numberOfSteps(123456789012345678901234))
print(numberOfSteps(1234567890123456789012345))
print(numberOfSteps(12345678901234567890123456))
print(numberOfSteps(123456789012345678901234567))
print(numberOfSteps(1234567890123456789012345678))
print(numberOfSteps(12345678901234567890123456789))
print(numberOfSteps(123456789012345678901234567890))
print(numberOfSteps(1234567890123456789012345678901))
print(numberOfSteps(12345678901234567890123456789012))
print(numberOfSteps(123456789012345678901234567890123))
print(numberOfSteps(1234567890123456789012345678901234))
print(numberOfSteps(12345678901234567890123456789012345))
print(numberOfSteps(123456789012345678901234567890123456))
print(numberOfSteps(1234567890123456789012345678901234567))
print

=======
Suggestion 4

def numberOfSteps (num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1
    return steps

print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))

=======
Suggestion 5

def solution(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = n - 1
            count += 1
    return count


print(solution(8))
print(solution(7))
print(solution(4))

=======
Suggestion 6

def numberOfSteps (num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1
    return steps

print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
print(numberOfSteps(123))
print(numberOfSteps(0))
print(numberOfSteps(1))
print(numberOfSteps(2))
print(numberOfSteps(3))
print(numberOfSteps(5))
print(numberOfSteps(10))
print(numberOfSteps(15))
print(numberOfSteps(20))
print(numberOfSteps(25))
print(numberOfSteps(30))
print(numberOfSteps(35))
print(numberOfSteps(40))
print(numberOfSteps(45))
print(numberOfSteps(50))
print(numberOfSteps(55))
print(numberOfSteps(60))
print(numberOfSteps(65))
print(numberOfSteps(70))
print(numberOfSteps(75))
print(numberOfSteps(80))
print(numberOfSteps(85))
print(numberOfSteps(90))
print(numberOfSteps(95))
print(numberOfSteps(100))
print(numberOfSteps(105))
print(numberOfSteps(110))
print(numberOfSteps(115))
print(numberOfSteps(120))
print(numberOfSteps(125))
print(numberOfSteps(130))
print(numberOfSteps(135))
print(numberOfSteps(140))
print(numberOfSteps(145))
print(numberOfSteps(150))
print(numberOfSteps(155))
print(numberOfSteps(160))
print(numberOfSteps(165))
print(numberOfSteps(170))
print(numberOfSteps(175))
print(numberOfSteps(180))
print(numberOfSteps(185))
print(numberOfSteps(190))
print(numberOfSteps(195))
print(numberOfSteps(200))
print(numberOfSteps(205))
print(numberOfSteps(210))
print(numberOfSteps(215))
print(numberOfSteps(220))
print(numberOfSteps(225))
print(numberOfSteps(230))
print(numberOfSteps(235))
print(numberOfSteps(240))
print(numberOfSteps(245))
print(numberOfSteps(250))
print(numberOfSteps(255))
print(numberOfSteps(260

=======
Suggestion 7

def minOperations(n):
    """
    :type n: int
    :rtype: int
    """
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n - 1
        operations += 1
    return operations

=======
Suggestion 8

def numberOfSteps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num -= 1
            count += 1
    return count

=======
Suggestion 9

def min_steps(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            if n == 3:
                count += 2
                break
            if (n + 1) % 4 == 0:
                n += 1
            else:
                n -= 1
        count += 1
    return count

n = 8
print(min_steps(n))

n = 7
print(min_steps(n))

n = 4
print(min_steps(n))

=======
Suggestion 10

def numberOfSteps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
            steps += 1
        else:
            num -= 1
            steps += 1
    return steps

print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
