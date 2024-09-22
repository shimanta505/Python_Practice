class Node:
    def __init__(self,data: int):
        self.data = data
        self.next = None # next pointer of node


class LinkedList:

    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None

    def insert_data(self,data: int):
         node: Node = Node(data)
         if self.__head is None:
             self.__head = node
             self.__tail = node
         else: # 200 > 300
             self.__tail.next = node
             self.__tail = node


    def print_List(self):
        head: Node = self.__head

        while head != None:
            print(f"Data : {head.data} >>>>> onj location {head.next}")
            head = head.next