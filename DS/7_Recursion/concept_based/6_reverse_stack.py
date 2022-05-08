# this problem is based on

# 5_sort an array problem


def minimize_the_input(stack):

    if not stack:
        return

    temp = stack.pop()

    minimize_the_input(stack)

    insert_at_starting(stack, temp)


def insert_at_starting(stack, temp):

    if len(stack) == 0:
        stack.append(temp)
        return

    cur_last_val = stack.pop()

    insert_at_starting(stack, temp)

    stack.append(cur_last_val)


stack = [1, 2, 3, 4, 5]

minimize_the_input(stack)

print(stack)
