""" in this problem we have to find that given array can be divided into 
2 part such that both sub-array sum == equal to each other

so we can take total of array and divide by 2 

then we have to check that given array can make half subarray 
such that sum of that subarray = half

(just converting into the subset problem)
"""


def equal_sum(arr, sum, n):

    if sum == 0:
        return True

    # reason to take n==0 instead of n<0
    # coz (in the recursion we are doing n-1)
    # which means when we are at n==1
    # then we are already subtracting 1 with it
    # n-1
    if n == 0:
        return False

    if sum >= arr[n - 1]:

        consider = equal_sum(arr, sum - arr[n - 1], n - 1)
        not_consider = equal_sum(arr, sum, n - 1)

        return consider or not_consider
    else:
        prev_return = equal_sum(arr, sum, n - 1)
        return prev_return


arr = [5, 3, 5, 11]
total = sum(arr)

if total & 1:
    print("Half cannot be found because total is odd")
else:
    half = total // 2
    n = len(arr)

    print(equal_sum(arr, half, n))
