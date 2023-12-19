def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count

if __name__ == '__main__':
    countDigitOne()