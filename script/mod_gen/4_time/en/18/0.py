def uniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    result = 91
    for i in range(3,n+1):
        result += (10-i+1)*factorial(9)//factorial(10-i)
    return result

if __name__ == '__main__':
    uniqueDigits()