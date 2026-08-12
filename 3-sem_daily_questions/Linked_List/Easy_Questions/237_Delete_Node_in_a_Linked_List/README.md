# 237. Delete Node in a Linked List

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; **LeetCode:** [#237](https://leetcode.com/problems/delete-node-in-a-linked-list/)

---

## Problem Statement

Delete a node from a singly linked list, but you are **NOT given access to the head** — only the node to be deleted is given.

The node to be deleted is **guaranteed to not be the tail**.

**Example:**
```
Input:  List = 4 → 5 → 1 → 9,  node = 5
Output: 4 → 1 → 9
```

---

## Approach — Copy-Next Trick

Normal deletion mein hum previous node ka `.next` change karte hain. But yahan `head` nahi diya — toh hum previous tak pahunch hi nahi sakte!

**Trick:** Delete karne ki jagah, **current node ko next node se overwrite karo**.

```python
node.val = node.next.val    # copy next node's value into current
node.next = node.next.next  # skip the next node
```

**Visualization:**
```
Before: ... → [5] → [1] → [9]
               ↑ delete this

Step 1: Copy next value:  ... → [1] → [1] → [9]
Step 2: Skip next node:   ... → [1] → [9]
```

---

## Why This Approach?

- Ye ek **classic trick** hai jab previous node ka access nahi hota
- Simply agle node ki value copy karo aur agle node ko hi delete kar do
- Previous node tak traversal ki zaroorat hi nahi padti

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(1)` — sirf 2 operations |
| **Space** | `O(1)` — no extra memory |

---

## Key Learning

> Jab node delete karni ho aur head na mile, toh **"delete" mat socho — "overwrite" socho**. Agle node ki value copy karo aur usse unlink karo.

> [!WARNING]
> Yeh trick **tail node** pe kaam nahi karti. Problem guarantee karti hai ki node tail nahi hoga.
