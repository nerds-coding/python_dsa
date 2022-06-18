# instead of this function we can use priority Q
def insert_in_sorting_order(stack, val):
    if not stack:
        stack.append(val)
    else:
        idx = 0
        for i in range(len(stack) - 1, -1, -1):
            if val > stack[-1]:
                return
            else:
                idx = i
        stack.insert(idx, val)


def k_smallest(arr, k):

    stack = list()

    for i in arr:
        insert_in_sorting_order(stack, i)

        if len(stack) > k:
            stack.pop()

    return stack


arr = [2, 5, 8, 9, 3, 6, 1]

print(k_smallest(arr, 2))
