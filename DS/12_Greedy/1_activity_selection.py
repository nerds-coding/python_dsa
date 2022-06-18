# https://practice.geeksforgeeks.org/tracks/DSASP-Greedy/?batchId=154&tab=1


def activity_selection(activity):

    total_activity_can_done = 1

    activity = sorted(activity, key=lambda x: x[1])

    prev = activity[0]
    for i in activity[1:]:
        if prev[1] <= i[0]:
            total_activity_can_done += 1
            prev = i

    return total_activity_can_done


activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
print(f"Total activity can be done = {activity_selection(activity)}")
