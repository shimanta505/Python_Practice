from dsa.dsa_double_linked_list.double_linked_list import DoubleLinkedList

if __name__ == '__main__':
    doubly_linked_list = DoubleLinkedList()
    doubly_linked_list.add(1)
    doubly_linked_list.add(2)
    doubly_linked_list.add(3)
    doubly_linked_list.add(4)
    doubly_linked_list.add(5)
    doubly_linked_list.add(6)
    doubly_linked_list.add(7)

    doubly_linked_list.print_doubly_linked_list()

    print(doubly_linked_list.remove_from_index(10))
    print(doubly_linked_list.length())
    doubly_linked_list.print_doubly_linked_list()
    print(doubly_linked_list.length())


