# 707. Design Linked List

> **Difficulty:** 🟡 Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; **LeetCode:** [#707](https://leetcode.com/problems/design-linked-list/)

---

## Problem Statement

Design your own linked list class (`MyLinkedList`) from scratch. Implement these operations:

- `get(index)` — Return the value at `index`. Return `-1` if invalid.
- `addAtHead(val)` — Insert `val` at the beginning.
- `addAtTail(val)` — Insert `val` at the end.
- `addAtIndex(index, val)` — Insert `val` before the `index`-th node.
- `deleteAtIndex(index)` — Delete the node at `index`.

---

## Approach — Custom Singly Linked List Class

Build a `Node` class and a `MyLinkedList` class that manages the entire list. Traverse from `head` to reach any index.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
```

**Key operations:**

```python
# get(index): traverse from head to index
def get(self, index):
    if self.head == None:
        return -1
    if index == 0:
        return self.head.val
    temp = self.head
    count = 0
    while temp and count < index:
        temp = temp.next
        count += 1
    if temp == None:
        return -1
    return temp.val

# addAtHead: new node → old head
def addAtHead(self, val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node

# addAtTail: traverse to end, append
def addAtTail(self, val):
    new_node = Node(val)
    if self.head == None:
        self.head = new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new_node

# addAtIndex: go to (index-1)th node, insert there
def addAtIndex(self, index, val):
    if index == 0:
        self.addAtHead(val)
        return
    new_node = Node(val)
    temp = self.head
    count = 0
    while temp and count < index - 1:
        temp = temp.next
        count += 1
    if temp == None:
        return
    new_node.next = temp.next
    temp.next = new_node

# deleteAtIndex: go to (index-1)th node, skip its next
def deleteAtIndex(self, index):
    if self.head == None:
        return
    if index == 0:
        self.head = self.head.next
        return
    temp = self.head
    count = 0
    while temp and count < index - 1:
        temp = temp.next
        count += 1
    if temp == None or temp.next == None:
        return
    temp.next = temp.next.next
```

---

## Why This Approach?

- Building a linked list from scratch is a **fundamental skill**
- Traversing from `head` to reach an index is the core pattern of linked lists
- Invalid index cases are handled gracefully with `-1` or early `return`

---

## Complexity

| Operation | Time | Space |
|---|---|---|
| `get` | `O(n)` | `O(1)` |
| `addAtHead` | `O(1)` | `O(1)` |
| `addAtTail` | `O(n)` | `O(1)` |
| `addAtIndex` | `O(n)` | `O(1)` |
| `deleteAtIndex` | `O(n)` | `O(1)` |
| Overall Space | — | `O(n)` |

---

## Key Learning

> For any index-based operation in a linked list, **traverse to `index - 1`** — then insert or delete from there. Random access like arrays is not possible in linked lists.
