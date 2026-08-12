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

Ek `Node` class banao aur ek `MyLinkedList` class jo poori list manage kare.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
```

**Key operations:**

```python
# get(index): traverse till index
def get(self, index):
    if index < 0 or index >= self.size:
        return -1
    curr = self.head
    for _ in range(index):
        curr = curr.next
    return curr.val

# addAtHead: new node → old head
def addAtHead(self, val):
    node = Node(val)
    node.next = self.head
    self.head = node
    self.size += 1

# addAtTail: traverse to end, append
def addAtTail(self, val):
    node = Node(val)
    if not self.head:
        self.head = node
    else:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    self.size += 1
```

---

## Why This Approach?

- Khud se linked list banana ek **fundamental skill** hai
- `size` track karna invalid index checks easy banata hai
- Operations ka time complexity samajh aata hai practically

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

> `size` counter hamesha maintain karo — invalid index handle karna bahut easy ho jaata hai. Aur **sentinel/dummy head node** use karoge toh edge cases (empty list, head insertion) aur bhi simple ho jaate hain.
