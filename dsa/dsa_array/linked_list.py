class _Node:
     def __init__(self,data: int):
         self.data = data
         self.next = None # next pointer of node


class LinkedList:

    def __init__(self):
        self.__head: _Node = None
        self.__tail: _Node = None

    def insert_data(self,data: int):
         node: _Node = _Node(data)
         if self.__head is None:
             self.__head = node
             self.__tail = node
         else: # 200 > 300
             self.__tail.next = node
             self.__tail = node



    def print_list(self):
        head: _Node = self.__head

        while head is not None:
            print(f"Data : {head.data} >>>>> onj location {head.next}")
            head = head.next