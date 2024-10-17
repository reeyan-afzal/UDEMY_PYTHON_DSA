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

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.nextptr = temp.nextptr
        temp.nextptr = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.insert(1, 7)
my_linked_list.print_list()

"""
Step 1: Initial state (LinkedList with 4 nodes):
  The current LinkedList looks like this:

  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3                               tail
  length = 4

-----------------------------------------------------

Step 2: insert(1, 7) call (inserting a new node with value 7 at index 1):
- The index 1 refers to the position between Node1 (index 0) and Node2 (index 1).
- First, the method checks if the index is out of bounds. Since index 1 is valid, the method continues.
- Since index 1 is neither 0 (prepend) nor equal to `length` (append), the insertion happens in the middle.
- A new node (`new_node`) is created with value 7.
- The `get(index - 1)` function is called to retrieve the node at index 0 (Node1), which is the node right before the desired insertion point.

  - Step 0: Start at Node1 (index 0).

- The new node's `nextptr` is set to Node1's current `nextptr` (which points to Node2).
- Node1’s `nextptr` is updated to point to the new node (Node7), effectively inserting the new node between Node1 and Node2.
- The list's length is increased by 1.

Before insert(1, 7):
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3                               tail

After insert(1, 7):
  [ Node1: 1 | nextptr -> Node7 ] --> [ Node7: 7 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node7                             Node2                              tail
  length = 5

- The method returns `True`, indicating that the node has been successfully inserted.

-----------------------------------------------------

Step 3: Printing the list:
  Calling `print_list()` will output:
  1
  7  (the newly inserted node with value 7 at index 1)
  2
  3
  4

-----------------------------------------------------

Final state:
  The LinkedList now reflects the insertion of the new node at index 1.

  head --> [ Node1: 1 | nextptr -> Node7 ] --> [ Node7: 7 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ] <-- tail
"""
