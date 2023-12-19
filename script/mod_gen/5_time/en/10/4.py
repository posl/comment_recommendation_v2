def eraseOverlapIntervals(intervals):
    intervals.sort()
    print(intervals)
    i = 0
    j = 1
    count = 0
    while j < len(intervals):
        if intervals[i][1] > intervals[j][0]:
            count += 1
            if intervals[i][1] > intervals[j][1]:
                i = j
            j += 1
        else:
            i = j
            j += 1
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapInt

if __name__ == '__main__':
    eraseOverlapIntervals()