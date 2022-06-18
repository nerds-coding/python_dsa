# https://stackoverflow.com/questions/32804626/recursive-function-to-sort-an-array

# this is to understand how to minimize the input and
# use DIVIDED and Conquer/ Utils funcitons


def smaller_the_input(arr, last_num):

    if len(arr) == 1:
        return

    last_num = arr.pop()

    smaller_the_input(arr, last_num)

    insert_by_order(arr, last_num)


def insert_by_order(arr, last_num):

    if len(arr) == 0 or arr[-1] <= last_num:
        arr.append(last_num)
        return

    bigger_val = arr.pop()
    insert_by_order(arr, last_num)
    arr.append(bigger_val)


arr = [3, 7, 5, 2]
smaller_the_input(arr, 0)

print(arr)

