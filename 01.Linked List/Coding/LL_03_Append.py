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


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

"""
Step 1: Initialize LinkedList with value 1:
 [ Node1: 1 | nextptr -> None ]
    ^
    | 
  head, tail (both point to the same node initially)
 length = 1

-----------------------------------------------------

Step 2: Append value 2:
 Before appending:
 [ Node1: 1 | nextptr -> None ] 
    ^
    | 
  head, tail

 After appending:
 [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
    ^                                ^
    |                                |
  head                             tail (now points to Node2)
 length = 2

-----------------------------------------------------

Step 3: Append value 3:
 Before appending:
 [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
    ^                                ^
    |                                |
  head                             tail

 After appending:
 [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> None ]
    ^                                ^                                  ^
    |                                |                                  |
  head                             Node2                             tail (now points to Node3)
 length = 3
"""

my_linked_list.print_list()
