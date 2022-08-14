def max_area_histogram(arr):
    n = len(arr)
    nsr = list()
    nsl = list()
    stack = list()

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

    nsr = nsr[::-1]
    max_area = 0

    for i in range(0, n):
        max_area = max((nsr[i] - nsl[i] - 1) * arr[i], max_area)

    return max_area


def max_area_binary_matrix(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, len(arr[i])):
            if arr[i][j]:
                arr[i][j] += arr[i - 1][j]
    max_area = 0
    for i in range(0, n):
        max_area = max(max_area_histogram(arr[i]), max_area)
    return max_area


A = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
print(max_area_binary_matrix(A))
