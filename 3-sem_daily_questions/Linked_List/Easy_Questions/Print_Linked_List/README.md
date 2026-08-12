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

`curr` pointer ko `head` se shuru karo aur tab tak aage badhate raho jab tak `curr` `None` na ho jaaye.

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

- Linked list ka **most fundamental operation** — traversal
- Har doosra linked list operation (search, insert, delete) traversal pe hi depend karta hai
- Array traverse se alag hai — `index` nahi, `curr.next` use karo

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — har node exactly ek baar visit |
| **Space** | `O(1)` — sirf ek pointer `curr` |

---

## Key Learning

> Array mein `arr[i]` se random access hoti hai. Linked list mein **random access possible nahi** — hamesha `head` se shuru karke traverse karo. Yahi linked list ki fundamental limitation hai (aur iska trade-off yeh hai ki insertion/deletion `O(1)` hoti hai array ke `O(n)` ke comparison mein).
