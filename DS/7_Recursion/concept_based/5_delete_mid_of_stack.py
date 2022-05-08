

def middle_stack(stack, n):

    if len(stack) == n // 2 + 1:
        stack.pop()
        return

    temp = stack.pop()
    middle_stack(stack, n)
    stack.append(temp)


stack = [1, 2, 3, 4]

middle_stack(stack, len(stack))

print(stack)
