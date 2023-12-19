def eraseOverlapIntervals(intervals):
    # Sort the intervals based on the end time
    intervals.sort(key=lambda x: x[1])
    # Keep track of the end time of the previous interval
    prev_end = intervals[0][1]
    # Keep track of the number of intervals that need to be removed
    count = 0
    # Iterate through the intervals
    for i in range(1, len(intervals)):
        # If the start time of the current interval is less than the end time of the previous interval
        if intervals[i][0] < prev_end:
            # Increment the count
            count += 1
        # Otherwise
        else:
            # Update the end time of the previous interval
            prev_end = intervals[i][1]
    # Return the count
    return count

if __name__ == '__main__':
    eraseOverlapIntervals()