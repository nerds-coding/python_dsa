# https://leetcode.com/problems/merge-two-sorted-lists/

# using inplace technique


def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val > list2.val:
        temp = list1
        list1 = list2
        list2 = temp

    ans = list1

    while list1 and list2:

        prev = None

        while list1 and list1.val <= list2.val:
            prev = list1
            list1 = list1.next

        prev.next = list2

        temp = list1
        list1 = list2
        list2 = temp

    return ans
