def stock_span_problem(arr):
    n = len(arr)
    stack = list()
    ans = list()

    for i in range(0, n):
        if len(stack) == 0:
            ans.append(1)
        elif stack[-1][0] > arr[i]:
            ans.append(i - stack[-1][1])
        else:
            while len(stack) > 0 and stack[-1][0] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                ans.append(1)
            else:
                ans.append(i - stack[-1][1])
        stack.append((arr[i], i))
        print(stack)

    return ans


print(stock_span_problem([100, 80, 60, 70, 60, 75, 80]))
#                        =[0,  1,  2,  3,  4,  5,  6]
#                         [1,  1,  1,  2,  1,  4,  6]
