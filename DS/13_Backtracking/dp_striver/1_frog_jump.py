# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?leftPanelTab=0

def frog_jump(n, arr):

    # if we reach the last then simply return the 0
    if n == 0:
        return 0

    # adding the prev return value with
    # abs one jump
    first = frog_jump(n - 1, arr) + abs(arr[n] - arr[n - 1])

    # if are at first index (0 base index)
    # then if make 2 jump it go in neg
    # so checking it in advance
    second = float("inf")
    if n > 1:
        second = frog_jump(n - 2, arr) + abs(arr[n] - arr[n - 2])

    # in answer we want min so returning the min
    # of first or second jumpy
    return min(first, second)
