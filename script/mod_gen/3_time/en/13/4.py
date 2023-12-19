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
