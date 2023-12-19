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

if __name__ == '__main__':
    min_operations()