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
