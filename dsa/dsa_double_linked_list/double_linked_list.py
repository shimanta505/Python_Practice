

class Node:
    def __init__(self,data: int):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __bool__(self):
        if self is None:
            pass

    def add(self,data: int):
        node: Node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node

        self.__size += 1


    def remove_from_index(self,index: int) -> int:
        if self.__head is None or self.__size <= index:
            return -1
        elif index == 0:
            self.remove_from_first()
        elif index == self.__size -1:
            self.remove_from_last()
        else:
            head : Node = self.__head


            while head is not None and index > 0:
                head = head.next
                index -= 1

            prevNode = head.prev
            nextNode = head.next
            # change the node location
            prevNode.next = nextNode
            nextNode.prev = prevNode

            self.__size -= 1

        return 0


    def print_doubly_linked_list(self):
        node: Node = self.__head

        while node is not None:
            print(f"prev [{node.prev}] current [{node.data}]")
            node = node.next

    def length(self) -> int:
        return self.__size

    def remove_from_first(self) -> int:
        if self.__head is None:
            return -1

        else:
            nextNode = self.__head.next
            nextNode.prev = None
            self.__head = nextNode

            self.__size -= 1
        return 0

    def remove_from_last(self) -> int:
        if self.__tail is None:
            return -1
        else:
            prevNode = self.__tail.prev
            prevNode.next = None
            self.__tail = prevNode

            self.__size -= 1
        return 0