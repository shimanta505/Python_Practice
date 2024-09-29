class ArrayStack:
    def __init__(self,size: int):
        self.size = size
        self.stack = [] * self.size
        self.top : int = -1

    def push(self,value : int):

        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top += 1
            self.stack[self.top] = value


    def pop(self):
        if self.top == -1:
            return "Empty"
        else:
            data = self.stack[self.top]
            self.top -= 1
            print(data)

