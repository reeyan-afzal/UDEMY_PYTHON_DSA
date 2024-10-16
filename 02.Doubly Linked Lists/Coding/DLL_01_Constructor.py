class Node:
    def __init__(self, value):
        self.value = value
        self.nextptr = None
        self.prevprt = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.nextptr


my_doubly_linked_list = DoublyLinkedList(4)
my_doubly_linked_list.print_list()
