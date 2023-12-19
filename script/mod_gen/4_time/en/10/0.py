def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prevEnd = float('-inf')
    for i in intervals:
        if i[0] >= prevEnd:
            prevEnd = i[1]
        else:
            count += 1
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print("The values above should be 1, 2, 0, 2, and 2.")

if __name__ == '__main__':
    eraseOverlapIntervals()