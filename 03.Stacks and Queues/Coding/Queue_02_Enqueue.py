class Node:
    def __init__(self, value):
        self.value = value
        self.nextptr = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.nextptr

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.nextptr = new_node
            self.last = new_node
        self.length += 1


my_queue = Queue(1)

my_queue.enqueue(2)

my_queue.print_queue()
