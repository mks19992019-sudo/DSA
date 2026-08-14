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

In normal deletion, we change the previous node's `.next`. But here `head` is not given — so we cannot reach the previous node!

**Trick:** Instead of deleting the current node, **overwrite it with the next node's value**.

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

- A **classic trick** when the previous node is not accessible
- Simply copy the next node's value and unlink the next node
- No traversal from the previous node is needed at all

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(1)` — only 2 operations |
| **Space** | `O(1)` — no extra memory |

---

## Key Learning

> When a node must be deleted but `head` is not available, **don't think "delete" — think "overwrite"**. Copy the next node's value and unlink it.

> [!WARNING]
> This trick does **not** work on the tail node. The problem guarantees the given node will never be the tail.
