from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mins = deque([2**64])

    def push(self, val: int) -> None:
        if val <= self.mins[-1]:
            self.mins.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        end = self.stack.pop()
        if self.mins[-1] == end:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
