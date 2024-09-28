from dsa.stack.linked_stack.linked_stack import LinkedStack

if __name__ == '__main__':
    linked_stack : LinkedStack = LinkedStack()
    linked_stack.push(1)
    linked_stack.push(2)
    linked_stack.push(3)
    linked_stack.push(4)
    linked_stack.push(5)

    linked_stack.traverse()
    print(">>>>>>>>>>>>>>>>>>")
    print(f"peek {linked_stack.peek()}")
    print(f"popp {linked_stack.pop()}")
    linked_stack.traverse()


