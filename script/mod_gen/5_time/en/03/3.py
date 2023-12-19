def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev = [1,1]
        for i in range(2,rowIndex+1):
            curr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(prev[j-1]+prev[j])
            prev = curr
        return curr

if __name__ == '__main__':
    getRow()