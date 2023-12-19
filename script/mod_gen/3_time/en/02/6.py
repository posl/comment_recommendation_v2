def generate(numRows):
    pascal = []
    for i in range(numRows):
        if i == 0:
            pascal.append([1])
        elif i == 1:
            pascal.append([1, 1])
        else:
            pascal.append([1])
            for j in range(len(pascal[i - 1]) - 1):
                pascal[i].append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            pascal[i].append(1)
    return pascal

if __name__ == '__main__':
    generate()