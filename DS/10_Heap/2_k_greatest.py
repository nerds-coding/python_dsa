# use can also use min_heap inseated of his function
def sort_in_descending_order(stack, val):

    if not stack:
        stack.append(val)
    else:
        idx = 0
        for i in range(len(stack) - 1, -1, -1):
            if val < stack[-1]:
                return
            else:
                idx = i

        stack.insert(idx, val)


def k_greatest_element(arr, k):
    stack = list()

    for i in arr:

        sort_in_descending_order(stack, i)

        if len(stack) > k:
            stack.pop()

    return stack[-1]


arr = [2, 5, 8, 9, 3, 6, 1]

print(k_greatest_element(arr, 2))
