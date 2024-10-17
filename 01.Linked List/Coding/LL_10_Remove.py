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

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.nextptr
        prev.nextptr = temp.nextptr
        temp.nextptr = None
        self.length -= 1
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.remove(2)
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

Step 2: remove(2) call (removing the node at index 2):
- The index 2 refers to Node3 in the list (indexing starts from 0).
- First, the method checks if the index is out of bounds. Since index 2 is valid, the method continues.
- Since index 2 is neither 0 (pop_first) nor equal to `length - 1` (pop), the removal happens in the middle.
- The `get(index - 1)` function is called to retrieve the node at index 1 (Node2), which is the node right before the one we want to remove.

  - Step 0: Start at Node1 (index 0).
  - Step 1: Move to Node2 (index 1).

- Once `prev` (Node2) is found, the `temp` pointer is assigned to Node2's `nextptr` (Node3).
- Node2’s `nextptr` is updated to skip over `temp` (Node3) and point to `temp.nextptr` (Node4).
- `temp`'s `nextptr` is set to `None` to detach it from the list.
- The list's length is decreased by 1.

Before remove(2):
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3 (target)                     tail

After remove(2):
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^
     |                                |                                  |
   head                             Node2                              tail
  length = 3

- The method returns `temp` (Node3), indicating that Node3 has been successfully removed.

-----------------------------------------------------

Step 3: Printing the result of remove(2):
  Since we are removing Node3, the removed node has value 3, and `remove()` will return Node3's value or reference.

-----------------------------------------------------

Final state:
  The LinkedList now reflects the removal of Node3 at index 2, and Node2’s `nextptr` points directly to Node4.

  head --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ] <-- tail
"""
