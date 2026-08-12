# Doubly Linked List Traversal

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Doubly Linked List

---

## Problem Statement

Traverse a **doubly linked list** in both directions — forward (head to tail) and backward (tail to head) — and print all node values.

**Example:**
```
List:     1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5

Forward:  1  2  3  4  5
Backward: 5  4  3  2  1
```

---

## Approach — Forward and Backward Pointer Walk

Doubly linked list mein har node ke paas `prev` aur `next` dono pointers hote hain.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # points to next node
        self.prev = None  # points to previous node
```

**Forward Traversal:**
```python
def traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" → ")
        curr = curr.next
```

**Backward Traversal:**
```python
def traverse_backward(tail):
    curr = tail
    while curr:
        print(curr.val, end=" → ")
        curr = curr.prev
```

---

## Why This Approach?

- Doubly linked list ka **main advantage** hi yahi hai — dono directions mein traverse kar sako
- `prev` pointer ki wajah se backward traversal **O(n)** mein possible hai (singly LL mein impossible without reversing)
- Browser history, undo/redo systems — real-world mein DLL isi liye use hoti hai

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — poori list ek baar traverse |
| **Space** | `O(1)` — sirf ek pointer variable |

---

## Key Learning

> Doubly Linked List ka **space trade-off** yeh hai: extra `prev` pointer rakhni padti hai (zyada memory), lekin **backward traversal free mein** mil jaata hai. Jab dono directions mein traversal chahiye toh DLL choose karo.
