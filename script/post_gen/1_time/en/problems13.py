Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1
    return steps

=======
Suggestion 2

def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + integerReplacement(n // 2)
    else:
        return 1 + min(integerReplacement(n + 1), integerReplacement(n - 1))
    
#Test Cases
integerReplacement(8) #3
integerReplacement(7) #4
integerReplacement(4) #2

=======
Suggestion 3

def numberOfSteps(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    return count

print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))

=======
Suggestion 4

def numSteps(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n += 1
        count += 1
    return count

=======
Suggestion 5

def minOperations(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    return count

=======
Suggestion 6

def numberOfSteps(num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            steps += 1
        else:
            num = num - 1
            steps += 1

    return steps

print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
print(numberOfSteps(123))
print(numberOfSteps(123456789))
print(numberOfSteps(1234567890))

=======
Suggestion 7

def integerReplacement(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + integerReplacement(n/2)
    else:
        return 1 + min(integerReplacement(n-1), integerReplacement(n+1))

=======
Suggestion 8

def sol(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + sol(n/2)
    else:
        return 1 + min(sol(n+1), sol(n-1))

print(sol(8))
print(sol(7))
print(sol(4))

=======
Suggestion 9

def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps

print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))
print(number_of_steps(123))
print(number_of_steps(0))
print(number_of_steps(1))
print(number_of_steps(2**31-1))

=======
Suggestion 10

def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """

    # if n is even, divide by 2
    # if n is odd, add or subtract 1
    # return the minimum number of operations to get to 1
    # 1 <= n <= 2^31 - 1

    # base case
    if n == 1:
        return 0
    # recursive case
    if n % 2 == 0:
        return 1 + integerReplacement(n / 2)
    else:
        return 1 + min(integerReplacement(n + 1), integerReplacement(n - 1))
