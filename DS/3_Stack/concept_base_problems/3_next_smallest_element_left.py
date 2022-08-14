[1, 3, 0, 0, 1, 2, 4]


def next_smallest_element_left(arr):
    stack = []
    ans = []

    n = len(arr)

    for i in range(0, n):
        if len(stack) == 0:
            ans.append(-1)
        elif len(stack) > 0 and stack[-1] < arr[i]:
            ans.append(stack[-1])
        else:
            while len(stack) > 0 and stack[-1] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(arr[i])

    return ans


print(next_smallest_element_left([1, 3, 0, 0, 1, 2, 4]))
#                                -1 ,1,-1,-1, 0, 1  ,2
