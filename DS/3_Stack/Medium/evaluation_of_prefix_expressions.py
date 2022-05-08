# https://www.tutorialspoint.com/evaluation-of-prefix-expressions-in-cplusplus
# prefixExp = "*+69-31"
# 30


def operator(op, temp1, temp2):
    if op == "+":
        return temp1 + temp2
    elif op == "-":
        return abs(temp2 - temp1)
    elif op == "*":
        return temp1 * temp2
    elif op == "/":
        return int(temp2 / temp1)
    else:
        return False


def evaluation_prefix_expression(arr):
    stack = list()
    n = len(arr)

    for i in range(n)[::-1]:
        if arr[i] not in ["+", "-", "*", "/"]:
            stack.append(int(arr[i]))
        else:
            stack.append(operator(arr[i], stack.pop(), stack.pop()))

    return stack.pop()


print(evaluation_prefix_expression("-+7*45+20"))
