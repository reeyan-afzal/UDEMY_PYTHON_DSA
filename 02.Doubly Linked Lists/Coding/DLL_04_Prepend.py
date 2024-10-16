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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nextptr = new_node
            new_node.prevprt = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prevprt
            self.tail.nextptr = None
            temp.prevprt = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nextptr = self.head
            self.head.prevprt = new_node
            self.head = new_node
        self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

my_doubly_linked_list.prepend(0)

my_doubly_linked_list.print_list()
