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


my_linked_list = LinkedList(2)
my_linked_list.append(1)

"""
Step 1: Initial state (before popping the first element):
  Current LinkedList:
  [ Node0: 0 | nextptr -> Node1 ] --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^                                  ^
     |                                |                                  |
   head                             Node1                              tail
  length = 3

-----------------------------------------------------

Step 2: First pop_first() call (removing the first node - Node0):
- `temp` points to the current `head` (Node0).
- `head` is updated to point to `head.nextptr` (Node1).
- Node0’s `nextptr` is set to `None`, detaching it from the list.
- The list's length is decreased by 1.

Before pop_first:
  [ Node0: 0 | nextptr -> Node1 ] --> [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^                                  ^
     |                                |                                  |
   head                             Node1                              tail

After pop_first:
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^
     |                                |
   head                             tail
  length = 2

- Node0 (with value 0) is returned by the function.
- `head` now points to Node1, and the `tail` remains at Node2.

-----------------------------------------------------

Step 3: Second pop_first() call (removing the first node - Node1):
- `temp` points to the current `head` (Node1).
- `head` is updated to point to `head.nextptr` (Node2).
- Node1’s `nextptr` is set to `None`, detaching it from the list.
- The list's length is decreased by 1.

Before pop_first:
  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> None ]
     ^                                ^
     |                                |
   head                             tail

After pop_first:
  [ Node2: 2 | nextptr -> None ]
     ^
     |
   head, tail
  length = 1

- Node1 (with value 1) is returned by the function.
- Both `head` and `tail` now point to the same node (Node2).

-----------------------------------------------------

Step 4: Third pop_first() call (removing the last node - Node2):
- `temp` points to the current `head` (Node2).
- `head` is updated to `None`, since there are no more nodes in the list.
- Node2’s `nextptr` is set to `None`, detaching it from the list.
- The list's length is decreased by 1, and since it becomes empty, `tail` is also set to `None`.

Before pop_first:
  [ Node2: 2 | nextptr -> None ]
     ^
     |
   head, tail

After pop_first:
  LinkedList is empty (head and tail are both None).
  length = 0

- Node2 (with value 2) is returned by the function.

-----------------------------------------------------

Final state:
  The LinkedList is now empty after popping all nodes.

  head --> None
  tail --> None
"""

print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
