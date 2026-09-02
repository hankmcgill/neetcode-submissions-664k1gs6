class MyStack:

    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        self.queue_2.append(x)
        while self.queue_1:
            self.queue_2.append(self.queue_1.popleft())
        temp = self.queue_1
        self.queue_1 = self.queue_2
        self.queue_2 = temp

    def pop(self) -> int:
        return self.queue_1.popleft()

    def top(self) -> int:
        return self.queue_1[0]

    def empty(self) -> bool:
        return not self.queue_1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()