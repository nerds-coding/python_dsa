#A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
# This means the last element inserted inside the stack is removed first.


# PUSH and POP = O(1)
# space complexity = O(n)


class Stack:

    def __init__(self): # defining Container for within the constructor
        self.top = -1 # to keep note of the current cursor in the stack
        self.stk = [] # stack itself
    
    def push(self,val): # to push the value in stack 
        self.top+=1 # updating the stack cursor
        self.stk.append(val)
    
    def pop(self): # to retreive the last element of the stack
        val = self.stk[self.top]
        del self.stk[self.top]
        self.top-=1 # also updating the stack cursor 
        return val # returning the value of stack
    
    def peek(self):# returning the stack top value
        return self.stk[self.top]
    
    def isEmpty(self): # checking the stack is empty or not
        return self.stk == []
    

stack = Stack() # making the stack object

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

print(stack.pop())
print(stack.peek())
print(stack.isEmpty())