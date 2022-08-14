# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1


# Explanation
# https://www.youtube.com/watch?v=DfljaUwZsOk

from collections import deque as dq


def max_of_subarrays(arr, n, k):
    l = r = 0
    q = dq()

    ans = list()

    while r < n:

        while q and arr[q[-1]] < arr[r]:
            q.pop()  # poping from back/end

        q.append(r)  # any-way we have to append the value

        # maintaining the windows  size
        if l > q[0]:
            q.popleft()  # removing from the front pop(0)

        if r + 1 >= k:
            ans.append(arr[q[0]])
            l += 1

        r += 1

    return ans
