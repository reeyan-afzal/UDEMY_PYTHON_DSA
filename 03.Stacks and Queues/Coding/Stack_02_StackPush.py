class Node:
    def __init__(self, value):
        self.value = value
        self.nextptr = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.nextptr

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.nextptr = self.top
            self.top = new_node
        self.height += 1


my_stack = Stack(1)
my_stack.push(2)

my_stack.print_stack()
