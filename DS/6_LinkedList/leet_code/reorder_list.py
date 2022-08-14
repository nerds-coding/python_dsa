# https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained


def reorderList(self, head):
    # step 1: find middle
    if not head:
        return []
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # step 2: reverse second half
    prev, curr = None, slow.next
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    slow.next = None

    # step 3: merge lists

    """
    [1,2,3,4] and [7,6,5]
    first element of head points to first element of h2
    then 
    we swap the 
    h1 and h2 among them 
    
    so
    
     now 1->7 and 7 points to 2 (which is now first element of h2)
     
     and then 
     we again we swap h1 and h2 
     
     so now 2 point to 6 (which now first element of h2)
     
     we keep swapping and pointing till get in the end of h2
    
    """
    head1, head2 = head, prev
    while head2:
        nextt = head1.next
        head1.next = head2
        head1 = head2
        head2 = nextt

    return head
