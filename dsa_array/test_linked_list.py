from dsa_array.linked_list import LinkedList

if __name__ == '__main__':
    linkedList: LinkedList = LinkedList()  # HEAD

    linkedList.insert_data(10)
    linkedList.insert_data(20)
    linkedList.insert_data(30)
    linkedList.insert_data(40)
    linkedList.insert_data(50)
    linkedList.insert_data(60)

    print("print the list >>>>>>>>>>")
    linkedList.print_List()
