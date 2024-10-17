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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nextptr = self.head
            self.head = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)

"""
Step 1: Initial state (before prepending):
  The current LinkedList has two nodes:

  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^
     |                                |
   head                             tail
  length = 2

-----------------------------------------------------

Step 2: Prepend operation (adding a new node with value 0 at the beginning):
- A new node, `new_node`, is created with value 0.
- Since the LinkedList is not empty (length > 0), the new node's `nextptr` is set to the current `head` (Node1).
- The `head` is then updated to point to the new node (Node0), making it the new first node.

Before prepend:
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^
     |                                |
   head                             tail

After prepend:
  [ Node0: 0 | nextptr -> Node1 ] --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^                                  ^
     |                                |                                  |
   head (new)                       Node1                              tail
  length = 3

-----------------------------------------------------

Step 3: Final state after prepending:
  The LinkedList now consists of three nodes, with the new node (Node0) added at the front.

  head --> [ Node0: 0 | nextptr -> Node1 ] --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ] <-- tail

  - The `head` now points to the newly prepended node (Node0).
  - The `tail` remains unchanged, still pointing to the last node (Node2).
  - The list's length has increased to 3.
"""


my_linked_list.print_list()
