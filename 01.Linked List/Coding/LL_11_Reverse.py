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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.nextptr
        before = None

        for _ in range(self.length):
            after = temp.nextptr
            temp.nextptr = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()

"""
Step 1: Initial state (LinkedList before reversal):
  The current LinkedList looks like this:

  [ Node1: 1 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
     ^                                ^                                  ^                                  ^
     |                                |                                  |                                  |
   head                             Node2                             Node3                               tail
  length = 4

-----------------------------------------------------

Step 2: reverse() call (reversing the LinkedList):
- The goal is to reverse the pointers such that the `head` becomes the `tail` and vice versa, with the nodes pointing in reverse order.

- Initial variables:
  - `temp`: points to the original `head` (Node1).
  - The `head` and `tail` are swapped: `self.head` is now Node4 and `self.tail` is now Node1.
  - `before`: initially set to `None` (used to reverse the pointer direction).
  - `after`: points to the next node after `temp` (Node2), to track the rest of the list as we reverse.

Step 3: Reversing process:
- The loop runs for the length of the LinkedList (4 iterations in this case).
- In each iteration:
  1. `after` stores the reference to the next node (next node after `temp`).
  2. `temp.nextptr` is reversed to point to `before`.
  3. `before` is updated to `temp` (previous node becomes the new "before").
  4. `temp` is updated to `after` (move to the next node in the original order).

**Iteration 1**:
  - `temp`: Node1
  - `after`: Node2
  - Reverse `temp.nextptr`: Node1 now points to `None` (since `before` is `None`).
  - Update `before` to Node1.
  - Move `temp` to `after` (Node2).

Current state after Iteration 1:
  [ Node1: 1 | nextptr -> None ]    [ Node2: 2 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
                                      ^                                ^                                  ^
                                      |                                |                                  |
                                    temp                            Node3                               tail

**Iteration 2**:
  - `temp`: Node2
  - `after`: Node3
  - Reverse `temp.nextptr`: Node2 now points to Node1 (reverse the pointer).
  - Update `before` to Node2.
  - Move `temp` to `after` (Node3).

Current state after Iteration 2:
  [ Node1: 1 | nextptr -> None ] <-- [ Node2: 2 | nextptr -> Node1 ]    [ Node3: 3 | nextptr -> Node4 ] --> [ Node4: 4 | nextptr -> None ]
                                                                        ^                                  ^
                                                                        |                                  |
                                                                      temp                               tail

**Iteration 3**:
  - `temp`: Node3
  - `after`: Node4
  - Reverse `temp.nextptr`: Node3 now points to Node2.
  - Update `before` to Node3.
  - Move `temp` to `after` (Node4).

Current state after Iteration 3:
  [ Node1: 1 | nextptr -> None ] <-- [ Node2: 2 | nextptr -> Node1 ] <-- [ Node3: 3 | nextptr -> Node2 ]    [ Node4: 4 | nextptr -> None ]
                                                                                                            ^
                                                                                                            |
                                                                                                          temp

**Iteration 4**:
  - `temp`: Node4
  - `after`: `None` (end of list)
  - Reverse `temp.nextptr`: Node4 now points to Node3.
  - Update `before` to Node4.
  - `temp` becomes `None` (end of loop).

Current state after Iteration 4:
  [ Node1: 1 | nextptr -> None ] <-- [ Node2: 2 | nextptr -> Node1 ] <-- [ Node3: 3 | nextptr -> Node2 ] <-- [ Node4: 4 | nextptr -> Node3 ]
     ^                                                                                                        ^
     |                                                                                                        |
   tail                                                                                                      head

- The loop completes, and the LinkedList is now fully reversed.
- `self.head` now points to Node4, and `self.tail` points to Node1, with the `nextptr` of each node reversed.

-----------------------------------------------------

Step 4: Final state (LinkedList after reversal):
  The LinkedList now looks like this:

  head --> [ Node4: 4 | nextptr -> Node3 ] --> [ Node3: 3 | nextptr -> Node2 ] --> [ Node2: 2 | nextptr -> Node1 ] --> [ Node1: 1 | nextptr -> None ] <-- tail
"""
