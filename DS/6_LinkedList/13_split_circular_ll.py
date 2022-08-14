# https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions


# https://www.youtube.com/watch?v=VdGIR91xlaM
def splitList(self, head, head1, head2):

    slow = head

    # so slow should alway point to second mid(in case odd value)
    fast = head.next

    while fast != head and fast.next != head:
        slow = slow.next
        fast = fast.next.next

    head2 = slow.next
    head1 = head
    slow.next = head

    cur = head2
    while cur.next != head:
        cur = cur.next

    cur.next = head2

    # this is to emulate pass by reference in python please don't delete below line.
    return head1, head2
