# Doubly Linked List Traversal

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Doubly Linked List

---

## Problem Statement

Traverse a **doubly linked list** in both directions — forward (head to tail) and backward (tail to head) — and return both sequences as a list.

**Example:**
```
List:     1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5

Forward:  [1, 2, 3, 4, 5]
Backward: [5, 4, 3, 2, 1]
```

---

## Approach — Two-Pass using `next` then `prev`

First traverse forward using the `next` pointer and stop at the last node. Then traverse backward from that point using the `prev` pointer.

```python
def displayList(head):
    a = []   # forward list
    b = []   # backward list
    temp = head

    # Forward pass: traverse to last node using .next
    while temp.next:
        a.append(temp.data)
        temp = temp.next
    a.append(temp.data)   # add the last node too

    # Backward pass: temp is now at tail, use .prev to go back
    while temp:
        b.append(temp.data)
        temp = temp.prev

    return [a, b]
```

**Visualization:**
```
List: 1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5

Forward pass (temp.next):
temp → 1 → 2 → 3 → 4 → 5
a = [1, 2, 3, 4, 5]      ← last node added with a.append(temp.data)

Backward pass (temp.prev), temp starts at 5:
temp → 5 → 4 → 3 → 2 → 1
b = [5, 4, 3, 2, 1]

Return: [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
```

---

## Why This Approach?

- The **main advantage** of a doubly linked list is traversal in both directions
- After the forward pass, `temp` is already at the tail — ready for backward traversal
- Backward traversal is **O(n)** thanks to the `prev` pointer (impossible in singly LL without reversing first)
- Real-world use cases: browser history, undo/redo systems

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — list is traversed twice (forward + backward) |
| **Space** | `O(n)` — both lists `a` and `b` store all elements |

---

## Key Learning

> The **trade-off** of a Doubly Linked List: it needs an extra `prev` pointer per node (more memory), but backward traversal comes for free. Choose DLL when traversal in both directions is needed.
