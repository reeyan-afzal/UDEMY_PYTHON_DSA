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

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.set_value(2, 0)
my_linked_list.print_list()

"""
Detailed visual representation of the LinkedList with the set_value() operation:

Step 1: Initial state (LinkedList with 4 nodes):
  The current LinkedList looks like this:

  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3                               tail
  length = 4

-----------------------------------------------------

Step 2: set_value(2, 0) call (updating the value at index 2):
- The index 2 refers to the third node in the list (indexing starts from 0).
- First, the method checks if the index is out of bounds (less than 0 or greater than or equal to the length). Since index 2 is valid, the method continues.
- The `get()` function is called to retrieve the node at index 2 (Node3, which has the current value 3).

  - Step 0: Start at Node1 (index 0).
  - Step 1: Move to Node2 (index 1).
  - Step 2: Move to Node3 (index 2).

- Once Node3 is found, its `value` is updated from 3 to 0.

Before set_value(2, 0):
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3 (value = 3)                  tail

After set_value(2, 0):
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 0 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3 (value updated to 0)         tail

- The method returns `True`, indicating that the value has been successfully updated.

-----------------------------------------------------

Step 3: Printing the list:
  Calling `print_list()` will output:
  1
  2
  0  (the value at index 2 has been updated)
  4

-----------------------------------------------------

Final state:
  The LinkedList now reflects the updated value at index 2.

  head --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 0 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ] <-- tail
"""
