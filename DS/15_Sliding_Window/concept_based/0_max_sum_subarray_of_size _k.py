# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


def maximumSumSubarray(self, K, arr, N):

    i = j = 0

    total = max_val = 0

    while j < N:

        total += arr[j]

        if j - i + 1 == K:  # to maintian the size of window
            max_val = max(max_val, total)

            total -= arr[i]
            i += 1
        j += 1

    return max_val
