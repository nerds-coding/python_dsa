class MinStack:
    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        """storing both value and minimum value in stack as tuple"""
        self.stack.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            # returning only value
            return self.stack[-1][0]

    def getMin(self) -> int:
        # returning only min value associated with tuple inside the stack
        if self.stack:
            return self.stack[-1][1]
        return 0
