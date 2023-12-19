def generate(numRows):
    pascal = []
    for i in range(numRows):
        pascal.append([])
        pascal[i].append(1)
        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        if(numRows != 0 and i != 0):
            pascal[i].append(1)
    return pascal
print(generate(5))
print(generate(1))
print(generate(0))
