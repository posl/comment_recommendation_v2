def solution(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n+1
        count += 1
    return count
print(solution(8)) #3
print(solution(7)) #4
print(solution(4)) #2
print(solution(1)) #0
print(solution(2)) #1
print(solution(3)) #2
print(solution(1000000000)) #32
print(solution(1000000001)) #33
print(solution(1000000002)) #33
print(solution(1000000003)) #34
print(solution(1000000004)) #33
print(solution(1000000005)) #34
print(solution(1000000006)) #34
print(solution(1000000007)) #35
print(solution(1000000008)) #34
print(solution(1000000009)) #35
print(solution(1000000010)) #35
print(solution(1000000011)) #36
print(solution(1000000012)) #35
print(solution(1000000013)) #36
print(solution(1000000014)) #36
print(solution(1000000015)) #37
print(solution(1000000016)) #36
print(solution(1000000017)) #37
print(solution(1000000018)) #37
print(solution(1000000019)) #38
print(solution(1000000020)) #37
print(solution(1000000021)) #38
print(solution(1000000022)) #38
print(solution(1000000023)) #39
print(solution(1000000024)) #38
print(solution(1000000025)) #39
print(solution(1000000026)) #39
print(solution(1000000027)) #40
print(solution(1000000028)) #39
print(solution(1000000029)) #40
print(solution(1000000030)) #40
print(solution(1000000031)) #41
print(solution(1000000032)) #40
print(solution(1000000033)) #41
print(solution(1000000034)) #41
print(solution(1000000035)) #42
print(solution(
