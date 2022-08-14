def count_subset(arr, val, n):

    if val == 0:
        return 1

    # reason to take n==0 instead of n<0
    # coz (in the recursion we are doing n-1)
    # which means when we are at n==1
    # then we are already subtracting 1 with it
    # n-1
    if n == 0:
        return 0

    if val >= arr[n - 1]:
        consider = count_subset(arr, val - arr[n - 1], n - 1)

        not_consider = count_subset(arr, val, n - 1)

        return consider + not_consider
    else:
        prev_possibility = count_subset(arr, val, n - 1)
        return prev_possibility


arr = [2, 3, 5, 6, 8, 10]
sum = 10
n = len(arr)

print(count_subset(arr, sum, n))
