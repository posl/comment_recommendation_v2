def problem(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            if (n + 1) % 4 == 0 and n != 3:
                n = n + 1
            else:
                n = n - 1
        count += 1
    return count
print(problem(8))
print(problem(7))
print(problem(4))
print(problem(123456789))
print(problem(1000000000))
print(problem(1000000001))
print(problem(1000000002))
print(problem(1000000003))
print(problem(1000000004))
print(problem(1000000005))
print(problem(1000000006))
print(problem(1000000007))
print(problem(1000000008))
print(problem(1000000009))
print(problem(1000000010))
print(problem(1000000011))
print(problem(1000000012))
print(problem(1000000013))
print(problem(1000000014))
print(problem(1000000015))
print(problem(1000000016))
print(problem(1000000017))
print(problem(1000000018))
print(problem(1000000019))
print(problem(1000000020))
print(problem(1000000021))
print(problem(1000000022))
print(problem(1000000023))
print(problem(1000000024))
print(problem(1000000025))
print(problem(1000000026))
print(problem(1000000027))
print(problem(1000000028))
print(problem(1000000029))
print(problem(1000000030))
print(problem(1000000031))
print(problem(1000000032))
print(problem(1000000033))
print(problem(1000000034))
print(problem(1000000035))
print(problem(1000000036))
print(problem(1000000037))
print(problem(1000000038))
print(problem(1000000039))
print(problem(1000000040))
print(problem(1000000041))
print(problem(1000000042))
print(problem(1000000043))
print(problem(1000000044))
print(problem(1000000045))
print(problem(1000000046))
print(problem(1000000047))
print(problem(1000000048))
