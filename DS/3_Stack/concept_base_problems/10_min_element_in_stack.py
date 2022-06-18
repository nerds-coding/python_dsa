class MinStack:
    def __init__(self):
        self.stack = list()
        self.low = 99999

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.low = val
        else:
            if val < self.low:
                self.stack.append(2 * val - self.stack[-1])
                self.min = val

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.min = 2 * self.min - self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack == []:
            return "null"
        else:
            return self.min
