def countDigitOne(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('1')
    return count

if __name__ == '__main__':
    countDigitOne()