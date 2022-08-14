# https://www.geeksforgeeks.org/find-k-closest-elements-given-value/


def max_heap(stack, val):

    if not stack:
        stack.append(val)
        return
    else:

        for i in range(len(stack) - 1, -1, -1):

            if val[0] > stack[i][0]:
                break

        # to handle if i == 0
        if stack[i][0] < val[0]:
            stack.insert(i + 1, val)
            return
        stack.insert(i, val)


def k_closet_element(arr, k, x):

    stack = list()

    for i in arr:

        max_heap(stack, [abs(i - x), i])

        if len(stack) > k:
            stack.pop()

    return stack


arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]

k = 4
x = 35

print(k_closet_element(arr, k, x))
