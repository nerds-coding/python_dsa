# we simply putting the index of next smallest element of LEft and right
# not found any smallest in left then -1 because there is no negative indexing
# but for the right side there is probablity ther last+1 index may have smaller


def max_area_histogram(arr):
    n = len(arr)
    nsr = list()
    nsl = list()
    stack = []

    for i in range(0, n):
        if len(stack) == 0:
            nsl.append(-1)
        elif stack[-1][0] < arr[i]:
            nsl.append(stack[-1][1])
        else:
            while len(stack) > 0 and stack[-1][0] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                nsl.append(-1)
            else:
                nsl.append(stack[-1][1])
        stack.append((arr[i], i))

    stack = []

    for i in range(n - 1, -1, -1):
        if len(stack) == 0:
            nsr.append(n)
        elif stack[-1][0] < arr[i]:
            nsr.append(stack[-1][1])
        else:
            while len(stack) > 0 and stack[-1][0] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                nsr.append(n)
            else:
                nsr.append(stack[-1][1])
        stack.append((arr[i], i))

    max_area = 0

    nsr = nsr[::-1]
    print(nsr)
    print(nsl)
    for i in range(0, n):
        max_area = max((nsr[i] - nsl[i] - 1) * arr[i], max_area)

    return max_area


print(max_area_histogram([6, 2, 5, 4, 5, 1, 6]))
