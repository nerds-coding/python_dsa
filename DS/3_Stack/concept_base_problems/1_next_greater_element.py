def next_greater_element(arr):
    stack = []  # to keep record of right side of array value
    ans = []  # to store th answer
    n = len(arr)

    for i in range(n - 1, -1, -1):
        # if stack is empty then there is no greater value in right
        # thus we inset -1 in answer
        if len(stack) == 0:
            ans.append(-1)

        # if last value is greater then current value of given array
        # then it is the most greater element to its right side
        elif len(stack) > 0 and stack[-1] > arr[i]:
            ans.append(stack[-1])

        elif len(stack) > 0 and stack[-1] <= arr[i]:

            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(arr[i])

    return ans[::-1]


print(next_greater_element([1, 3, 0, 0, 1, 2, 4]))
