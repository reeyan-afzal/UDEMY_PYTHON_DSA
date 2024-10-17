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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.nextptr
        temp.nextptr = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.nextptr
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()
print(my_linked_list.get(2))

"""
Detailed visual representation of the LinkedList with the get() operation:

Step 1: Initial state (LinkedList with 4 nodes):
  After initializing and appending values, the current LinkedList looks like this:

  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3                               tail
  length = 4

-----------------------------------------------------

Step 2: Printing the list:
  Calling `print_list()` will output:
  1
  2
  3
  4

-----------------------------------------------------

Step 3: get(2) call (retrieving the node at index 2):
- The index 2 refers to the third node (indexing starts from 0).
- First, the method checks if the index is out of bounds (less than 0 or greater than or equal to the length), which it isn’t in this case (index 2 is valid).
- A temporary pointer `temp` starts at the `head` (Node1).
- The method traverses the list by moving the pointer 2 steps forward:

  - Step 0: `temp` is at Node1.
  - Step 1: `temp` moves to Node2.
  - Step 2: `temp` moves to Node3.

- The method returns the node at index 2 (Node3), which has the value 3.

Before get(2):
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3 (target node)                tail

After get(2):
  The method returns the Node3 with value 3.
  Output: <Node object at memory_address> (showing the object reference, not the actual node structure).
  You can access the value via `my_linked_list.get(2).value`, which would return 3.

-----------------------------------------------------

Final state:
  No changes are made to the list after the `get()` operation. The structure remains the same.

  head --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ] <-- tail
"""
