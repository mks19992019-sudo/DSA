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

Har node ke `prev` aur `next` pointers ko **swap** karo, phir `prev` (jo pehle `next` tha) ke saath aage badho.

```python
def reverse_doubly_linked_list(head):
    curr = head
    new_head = None

    while curr:
        # Swap prev and next pointers
        curr.prev, curr.next = curr.next, curr.prev

        # Move to the next node (which is now curr.prev after swap)
        new_head = curr
        curr = curr.prev

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

- Singly LL reverse karne mein `prev`, `curr`, `next_node` teen pointers chahiye the
- DLL mein `prev` pointer **already har node mein hota hai** — sirf swap karna hai
- Ek hi pass, in-place, no extra memory

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — har node exactly ek baar visit |
| **Space** | `O(1)` — in-place swap, no extra memory |

---

## Key Learning

> Singly LL reverse = **pointer redirection** (3 pointers) \
> Doubly LL reverse = **pointer swap** (directly swap prev ↔ next)\
> DLL reverse Singly LL reverse se **conceptually simpler** hai kyunki `prev` pointer already available hai.
