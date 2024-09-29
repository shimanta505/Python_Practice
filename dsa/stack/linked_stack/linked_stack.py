class _Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.top is None

    def push(self,data):
        node : _Node = _Node(data)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def traverse(self):
        head : _Node = self.top
        while head is not None:
            print(f"|{head.data}|")
            head = head.next

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.top.data

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data

