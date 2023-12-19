def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
    return pascal
print(generate(5))
print(generate(1))
