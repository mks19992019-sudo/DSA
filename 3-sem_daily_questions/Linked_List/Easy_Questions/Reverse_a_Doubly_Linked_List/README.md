# Reverse a Doubly Linked List

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Doubly Linked List

---

## Problem Statement

Given the head of a **doubly linked list**, reverse it so that the old tail becomes the new head, and all `prev`/`next` pointers are swapped.

**Example:**
```
Before: 1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5
After:  5 ⇄ 4 ⇄ 3 ⇄ 2 ⇄ 1
```

---

## Approach — Swap `prev` and `next` at Each Node

Swap the `prev` and `next` pointers at every node, then move to the next node via `prev` (which now holds the original `next` after the swap).

```python
def reverse(head):
    temp = head
    new_head = head

    while temp:
        # Swap prev and next pointers
        temp.next, temp.prev = temp.prev, temp.next

        # Move to next node (now stored in temp.prev after swap)
        new_head = temp
        temp = temp.prev

    return new_head
```

**Step-by-step on `1 ⇄ 2 ⇄ 3`:**
```
Node 1: prev=None, next=2  →  swap  →  prev=2, next=None
Node 2: prev=1,    next=3  →  swap  →  prev=3, next=1
Node 3: prev=2,    next=None → swap → prev=None, next=2   ← new head!

Result: 3 ⇄ 2 ⇄ 1 ✓
```

---

## Why This Approach?

- Reversing a singly LL required three separate pointers (`prev`, `curr`, `next_node`)
- In a DLL, the `prev` pointer is **already present in every node** — just swap it
- Single pass, in-place, no extra memory needed

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — every node is visited exactly once |
| **Space** | `O(1)` — in-place swap, no extra memory |

---

## Key Learning

> Singly LL reverse = **pointer redirection** (3 separate pointers) \
> Doubly LL reverse = **pointer swap** (directly swap prev ↔ next) \
> DLL reversal is **conceptually simpler** than singly LL reversal because the `prev` pointer is already available.
