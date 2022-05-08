# https://www.techiedelight.com/find-subarray-having-given-sum-given-array/


# Function to check if a sublist with the given sum exists in the list or not
def findSublist(nums, target):
    # create an empty set
    s = set()
    # insert number 0 into the set to handle the case when a
    # sublist with the given sum starts from index 0
    s.add(0)
    # keep track of the sum of elements so far
    sum_so_far = 0
    # traverse the given list
    for i in nums:
        # update sum_so_far
        sum_so_far += i
        # if `sum_so_far - target` is seen before, we have found
        # the sublist with sum equal to `target`
        if (sum_so_far - target) in s:
            return True
        # otherwise, search the sum of elements so far in the set
        s.add(sum_so_far)
    # we reach here when no sublist exists
    return False


if __name__ == "__main__":

    # a list of integers
    nums = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    target = -3

    print(findSublist(nums, target))
