def infix_to_prefix(arr):
    n = len(arr)
    stack = list()
    order = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    ans = ""
    arr = arr[::-1]

    for i in range(n):
        if arr[i] != " ":
            if arr[i].isalpha():
                ans += arr[i]
            elif arr[i] == ")":
                stack.append(arr[i])
            elif arr[i] == "(":
                while stack and stack[-1] != ")":
                    ans += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != ")" and order[stack[-1]] >= order[arr[i]]:
                    ans += stack.pop()

                stack.append(arr[i])

    while stack:
        ans += stack.pop()
    return ans[::-1]


print(infix_to_prefix("(A - B/C) * (A/K-L)"))
