# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/


def getIntersectionNode(headA, headB):

    l1 = headA
    l2 = headB

    while l1 != l2:

        l1 = l1.next if (l1) else headB
        l2 = l2.next if (l2) else headA

    return l1

