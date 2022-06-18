def sort_array(arr):
    i = 0
    while i < len(arr):

        # If the current element is
        # at correct position
        if arr[i] == i + 1:
            i += 1

        # Else swap the current element
        # with it's correct position
        else:

            # Swap the value of
            # arr[i] and arr[arr[i]-1]
            temp1 = arr[i]
            temp2 = arr[arr[i] - 1]
            arr[i] = temp2
            arr[temp1 - 1] = temp1
    return arr


print(sort_array([3, 4, 5, 2, 1]))
