# delete the Nth last node

"""
Input: 2 -> 3 -> 1 -> 7 -> NULL, N = 1 
Output: 
The created linked list is: 
2 3 1 7 
The linked list after deletion is: 
2 3 1

Input: 1 -> 2 -> 3 -> 4 -> NULL, N = 4 
Output: 
The created linked list is: 
1 2 3 4 
The linked list after deletion is: 
2 3 4 

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head

        self.head = node

    def print_all_node(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def delete_nth_last_node(self, loc):
        count = 0
        temp = self.head

        while temp:
            count += 1

            temp = temp.next

        loc = count - loc

        if loc == 0:
            self.head = self.head.next
            return self.head

        temp = self.head
        prev = None

        while loc:
            prev = temp
            temp = temp.next

            loc -= 1

        if temp.next:
            prev.next = temp.next
        else:
            prev.next = None
        return self.head


ll = LinkedList()

ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)
ll.insert_at_head(5)
ll.insert_at_head(6)
ll.insert_at_head(7)


ll.delete_nth_last_node(7)

ll.print_all_node()
