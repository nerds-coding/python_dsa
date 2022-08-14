def longest_valid_parenthesis(arr):
    n = len(arr)
    stack = list()

    closing = [")", "}", "]"]
    pairs = ["()", "[]", "{}"]

    count = 0
    for i in range(0, n):
        if arr[i] in closing:
            if stack:
                if stack.pop() + arr[i] in pairs:
                    count += 2
        else:
            stack.append(arr[i])

    return count


print(longest_valid_parenthesis("((()"))
