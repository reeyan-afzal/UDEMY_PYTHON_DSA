class Node:
    def __init__(self, value):
        self.value = value
        self.nextptr = None


class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nextptr = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.nextptr:
            pre = temp
            temp = temp.nextptr
        self.tail = pre
        self.tail.nextptr = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.pop()

my_linked_list.print_list()
