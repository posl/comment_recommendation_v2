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
