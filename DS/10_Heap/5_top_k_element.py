def min_heap(stack, val):
    if not stack:
        stack.append(val)
    else:

        stack.append(val)

        for i in range(len(stack) - 1, 0, -1):

            if stack[i][1] > stack[i - 1][1]:
                stack[i - 1][1], stack[i][1] = stack[i][1], stack[i - 1][1]
            else:
                break


def top_k_element(arr, k):

    stack = list()

    count = {}
    for i in arr:

        if count.get(i):
            count[i] += 1
        else:
            count[i] = 1

    for key, val in count.items():
        min_heap(stack, [key, val])

        if len(stack) > k:
            stack.pop()

    return stack


arr = [1, 1, 1, 2, 2, 3, 3, 4]

print(top_k_element(arr, 2))
