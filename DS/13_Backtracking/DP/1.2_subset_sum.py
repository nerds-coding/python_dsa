# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/


def subset_sum(target, arr, n):

    if target == 0:
        return True
    # reason to take n==0 instead of n<0
    # coz (in the recursion we are doing n-1)
    # which means when we are at n==1
    # then we are already subtracting 1 with it
    # n-1
    if n == 0:
        return False

    if target >= arr[n-1]:

        consider = subset_sum(target - arr[n-1], arr, n - 1)
        not_consider = subset_sum(target, arr, n - 1)

        return consider or not_consider
    else:
        return subset_sum(target, arr, n - 1)


arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(arr)

print(subset_sum(sum, arr, n))
