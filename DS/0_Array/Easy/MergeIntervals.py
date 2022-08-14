    """
    
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    
    """


def merge(intervals):
    intervals.sort()
    i = 0
    while i != len(intervals) - 1:
        if (intervals[i + 1][0]) in range(intervals[i][0], intervals[i][1] + 1):
            x = [
                min(intervals[i][0], intervals[i + 1][0]),
                max(intervals[i + 1][1], intervals[i][1]),
            ]
            intervals.pop(i + 1)
            intervals.pop(i)
            intervals.insert(i, x)

        else:
            i += 1
            # print(i,intervals)
    return intervals
