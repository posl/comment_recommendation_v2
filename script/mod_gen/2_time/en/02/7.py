def generate(numRows):
    #create list of lists
    result = [[1]]
    #loop through the rows
    for i in range(1, numRows):
        #create the row
        row = [1]
        #loop through the columns
        for j in range(1, i):
            #add the sum of the previous row's j and j-1
            row.append(result[i-1][j] + result[i-1][j-1])
        #add the last 1 to the row
        row.append(1)
        #add the row to the result
        result.append(row)
    return result
print(generate(5))
print(generate(1))
print(generate(0))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(6))
print(generate(7))
print(generate(8))
print(generate(9))
print(generate(10))
print(generate(11))
print(generate(12))
print(generate(13))
print(generate(14))
print(generate(15))
print(generate(16))
print(generate(17))
print(generate(18))
print(generate(19))
print(generate(20))
print(generate(21))
print(generate(22))
print(generate(23))
print(generate(24))
print(generate(25))
print(generate(26))
print(generate(27))
print(generate(28))
print(generate(29))
print(generate(30))
