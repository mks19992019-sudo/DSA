# Check If Linked List is Circular

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Circular Detection

---

## Problem Statement

Given the head of a linked list, determine whether it is **circular** (i.e., the last node's `.next` points back to the `head`, forming a complete loop).

**Example:**
```
Circular:     1 → 2 → 3 → 4
              ↑               |
              └───────────────┘

Not Circular: 1 → 2 → 3 → None
```

---

## Approach — Normal Traversal (temp == head)

Start a `temp` pointer from `head.next` and keep traversing:
- If `temp == head` is found, the list is circular → return `True`
- If `temp == None` is found first, the list is not circular → return `False`

```python
def isCircular(head):
    temp = head

    while True:
        temp = temp.next
        if temp == None:
            break
        if temp == head:
            return True
    return False
```

**Visualization:**
```
Circular case:
head → [1] → [2] → [3] → [4] → (back to head)
        ↑                          ↑
       start                 temp == head → True ✓

Non-circular case:
head → [1] → [2] → [3] → None
                           ↑
                      temp == None → False ✓
```

---

## Why This Approach?

- Simplest and most direct approach for circular linked list detection
- In a circular list, the last node's `.next` points exactly to `head` — just check for that
- `temp == head` directly detects whether the list forms a complete loop
- Perfect for singly linked lists where the structure is guaranteed to be either fully circular or non-circular

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — traverses the list once |
| **Space** | `O(1)` — only one `temp` pointer |

---

## Key Learning

> The straightforward way to detect a circular list — start from `head`, move one step at a time, and check if `temp` comes back to `head`. If `None` is encountered first, the list is not circular.
