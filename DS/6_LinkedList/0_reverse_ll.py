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

    def reverse_ll(self):
        if(not head):
            return head
        
        prev = None
        temp = head
        
        while(temp):
            cur = temp
            temp = temp.next
            
            cur.next = prev
            prev = cur
        
        return prev


ll = LinkedList()

ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)
ll.insert_at_head(5)
ll.insert_at_head(6)
ll.insert_at_head(7)

# ll.print_all_node()

print("reverse")
ll.reverse_ll()
ll.print_all_node()
