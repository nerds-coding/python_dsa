def max_heap(stack, val):

    stack.append(val)

    for i in range(len(stack) - 1, 0, -1):

        if stack[i] < stack[i - 1]:
            stack[i], stack[i - 1] = stack[i - 1], stack[i]
        else:
            break


def sum_between_k_smallest(arr, k):

    stack = list()

    for i in arr:

        max_heap(stack, i)

    return stack[k - 1]


arr = [1, 3, 5, 11, 12, 15]

f1 = sum_between_k_smallest(arr, 3)
f2 = sum_between_k_smallest(arr, 6)

ans = 0
for i in arr:
    if (i < f2) and (i > f1):
        ans += i

print(ans)
