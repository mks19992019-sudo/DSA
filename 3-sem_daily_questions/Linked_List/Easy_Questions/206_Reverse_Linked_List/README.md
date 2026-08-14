# 206. Reverse Linked List

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; **LeetCode:** [#206](https://leetcode.com/problems/reverse-linked-list/)

---

## Problem Statement

Given the head of a singly linked list, reverse the list and return the reversed list.

**Example:**
```
Input:  1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1
```

---

## Approach — Iterative Pointer Reversal

Use three pointers: `prev`, `curr`, and `Next`.

```python
prev = None
curr = head

while curr:
    Next = curr.next    # save next
    curr.next = prev    # reverse the link
    prev = curr         # move prev forward
    curr = Next         # move curr forward

return prev  # new head
```

**Visualization:**
```
Initial:  None ← 1 → 2 → 3 → 4 → 5
Step 1:   None ← 1  2 → 3 → 4 → 5   (prev=1, curr=2)
Step 2:   None ← 1 ← 2  3 → 4 → 5   (prev=2, curr=3)
...
Final:    None ← 1 ← 2 ← 3 ← 4 ← 5  (prev=5 = new head)
```

---

## Why This Approach?

- **In-place** — no extra list or stack needed
- **One pass** — done in a single traversal
- Recursive approach also works but uses extra O(n) call stack space — iterative is more optimal

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — traverses the list once |
| **Space** | `O(1)` — only 3 pointers, no extra memory |

---

## Key Learning

> When reversing links, **save `next` before reversing** — otherwise the chain breaks and the rest of the list is lost.
