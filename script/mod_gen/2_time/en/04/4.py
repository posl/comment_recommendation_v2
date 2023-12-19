def countBits(n):
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result

if __name__ == '__main__':
    countBits()