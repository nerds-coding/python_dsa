# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1


def printFirstNegativeInteger(arr, n, k):

    i = j = 0

    q = list()
    ans = list()
    while j < n:

        # we will push those values who r negative
        if arr[j] < 0:
            q.append(arr[j])

        if j - i + 1 == k:

            if q:
                if arr[i] == q[0]:  # preventing from printing same anwer twice
                    # remove those values which are now not in window size
                    ans.append(q.pop(0))
                else:
                    # if values are inside the window then simply
                    # append that values
                    ans.append(q[0])
            else:
                # if there is not value simply return 0
                ans.append(0)

            i += 1
        j += 1

    return ans
