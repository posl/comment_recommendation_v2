def generate(numRows):
    result = []
    for i in range(numRows):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row)-1):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result
print(generate(5))
print(generate(1))
