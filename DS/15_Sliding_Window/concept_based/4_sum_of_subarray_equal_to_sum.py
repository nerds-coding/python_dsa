# catch and release technique

"""
    where j we use to catch new item from the given arr/string
    
    and i is used when len(of j dict) > k 
    
    
    so we release from ans-> dict/string/arr usign i
    
    till the len == k


"""


def lenOfLongSubarr(A, N, K):

    # k = sum (given)
    i, j, sum = 0, 0, 0
    maxLen = float("inf")

    while j < N:
        sum += A[j]
        if sum < K:
            j += 1
        elif sum == K:
            maxLen = max(maxLen, j - i + 1)
            j += 1
        elif sum > K:
            # if sum got greater then k
            # then we should subtract from the back
            # to maintian  the window size

            while sum > K:
                sum -= A[i]
                i += 1
            if sum == K:
                maxLen = max(maxLen, j - i + 1)
            j += 1
    return maxLen


# Driver Code
arr = [10, 5, 2, 7, 1, 9]
n = len(arr)
k = 15
print("Length = " + str(lenOfLongSubarr(arr, n, k)))
