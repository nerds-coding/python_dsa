def next_smallest_element_right(arr):
    ans = []
    stack = []

    n = len(arr)

    for i in range(n - 1, -1, -1):
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

    return ans[::-1]


print(next_smallest_element_right([4, 2, 1, 0, 0, 3, 1]))
#                                  2, 1, 0,-1,-1, 1, -1
