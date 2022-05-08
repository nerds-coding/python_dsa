# https://leetcode.com/problems/remove-linked-list-elements/


"""

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
    
"""


def removeElements(head, val):
    if not head:
        return head

    # movning head till val match the head
    # if head == val then we have to move
    # till we found any other node which another val

    """
    eg -
        Input: head = [7,7,7,7], val = 7
        Output: []
    
    """
    while head and head.val == val:
        head = head.next

    cur = head
    temp = cur

    """  
    checking current value == val and 
    also cur.next is also not None (b'coz we have to point current node to next if 
    
    cur.val == val)
    
    """
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next  # we just point ptr to next
            # not changing the current value
            # so we can check the current val also

        else:
            cur = cur.next

    return temp
