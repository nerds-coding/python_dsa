def min_heap(stack, val):

    stack.append(val)

    for i in range(len(stack) - 1, 0, -1):

        if stack[i][0] < stack[i - 1][0]:
            stack[i], stack[i - 1] = stack[i - 1], stack[i]
        else:
            break


def k_closet_point_origin(arr, k):

    stack = list()

    close = list()

    for i in range(len(arr)):
        
        sqr = arr[i][0] ** 2 + arr[i][1] ** 2
        close.append((sqr, arr[i]))

        min_heap(stack, close[-1])

        if len(stack) > k:
            stack.pop()

    return stack


arr = [[1, 2], [-2, 2], [5, 8], [0, 1]]

print(k_closet_point_origin(arr, 2))
