# https://www.youtube.com/watch?v=dYfM6J1y0mU&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9&index=4


def min_heap(stack, val):

    if not stack:
        stack.append(val)
    else:

        i = 0
        if stack[-1] > val:
            stack.append(val)
            return
        for i in range(len(stack) - 1, -1, -1):

            if val < stack[i]:
                break

        if stack[i] > val:  # for corner case where i == 0
            stack.insert(i + 1, val)
            return
        stack.insert(i, val)


def k_sorted_array(arr, k):

    stack = list()

    j = 0
    for i in arr:

        min_heap(stack, i)

        if len(stack) > k:
            arr[j] = stack.pop()
            j += 1

    while stack:
        arr[j] = stack.pop()
        j += 1

    return arr


arr = [6, 5, 3, 2, 8, 10, 9, 7]

print(k_sorted_array(arr, 4))
