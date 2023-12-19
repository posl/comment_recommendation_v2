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

if __name__ == '__main__':
    solution()