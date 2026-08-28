class Node:
    def __init__(self, val: int):
        self.val = val
        self.nxt = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size <= index:
            return -1
        
        curr = self.head
        for i in range(index + 1):
            if i == index:
                return curr.val
            i += 1
            if curr.nxt:
                curr = curr.nxt
            else:
                return -1

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head, self.tail = new, new
        else:
            curr_head = self.head
            curr_head.prev = new
            new.nxt = curr_head
            self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.addAtHead(val)
            return
        else:
            curr_tail = self.tail
            curr_tail.nxt = new
            new.prev = curr_tail
            self.tail = new
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            curr = self.head
            for i in range(index + 1):
                if i == index - 1:
                    new = Node(val)
                    temp = curr.nxt
                    temp.prev = new
                    new.nxt = temp
                    curr.nxt = new
                    new.prev = curr
                    self.size += 1
                curr = curr.nxt

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:
            return
        if index == 0:
            curr_head = self.head
            curr_head.nxt.prev = None
            self.head = curr_head.nxt
            del curr_head
        elif self.size == 1:
            curr = self.head
            del curr
        elif index == (self.size - 1):
            curr_tail = self.tail
            curr_tail.prev.nxt = None
            self.tail = curr_tail.prev
            del curr_tail
        else:
            curr = self.head
            for i in range(index + 1):
                if i == index - 1:
                    temp_nxt = curr.nxt
                    temp_nxt.prev = curr
                    curr.nxt = temp_nxt.nxt
                    del temp_nxt
                curr = curr.nxt
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)