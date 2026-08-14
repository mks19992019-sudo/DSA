# Print Linked List

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Traversal

---

## Problem Statement

Given the head of a singly linked list, print all the node values from head to tail.

**Example:**
```
Input:  1 → 2 → 3 → 4 → 5 → None
Output: 1 2 3 4 5
```

---

## Approach — Simple Traversal

Start a `curr` pointer at `head` and keep moving forward until `curr` becomes `None`.

```python
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()  # newline at end
```

**Visualization:**
```
curr → [1] → [2] → [3] → [4] → [5] → None
        ↑
      print 1, move curr

curr →  [1] → [2] → [3] → [4] → [5] → None
               ↑
             print 2, move curr
... and so on
```

---

## Why This Approach?

- Traversal is the **most fundamental operation** of a linked list
- Every other linked list operation (search, insert, delete) depends on traversal
- Different from array traversal — use `curr.next` instead of an index

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — every node is visited exactly once |
| **Space** | `O(1)` — only one pointer `curr` |

---

## Key Learning

> Arrays allow `arr[i]` random access. Linked lists do **not support random access** — always start from `head` and traverse. This is the fundamental limitation of linked lists (the trade-off being that insertion/deletion is `O(1)` vs `O(n)` in arrays).
