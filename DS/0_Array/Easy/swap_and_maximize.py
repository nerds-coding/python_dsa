# https://practice.geeksforgeeks.org/problems/swap-and-maximize5859/1/?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions#


# N = 4
# a[] = {4, 2, 1, 8}

def maxSum(arr, n):
    arr.sort()

    ans = 0

    i = 0
    j = n - 1

    """
    After sorting we r taking absloute of first and last 
    2 get max sum
    """

    while i < j:
        ans += arr[j] - arr[i]
        i += 1

        ans += arr[j] - arr[i]
        j -= 1

    ans += arr[i] - arr[0]

    return ans
