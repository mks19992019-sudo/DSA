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

Teen pointers use karte hain: `prev`, `curr`, aur `next_node`.

```
prev = None
curr = head

while curr:
    next_node = curr.next   # save next
    curr.next = prev        # reverse the link
    prev = curr             # move prev forward
    curr = next_node        # move curr forward

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

- **In-place** — no extra list ya stack nahi chahiye
- **One pass** — single traversal mein kaam ho jaata hai
- Recursive approach bhi hoti hai but extra O(n) call stack use karti hai — iterative zyada optimal hai

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — ek baar poori list traverse karti hai |
| **Space** | `O(1)` — sirf 3 pointers, no extra memory |

---

## Key Learning

> Link reverse karte waqt **pehle next save karo**, tab hi reverse karo — warna chain toot jaati hai aur baaki list kho jaati hai.
