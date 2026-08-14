# Linked List — End Insertion

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Insertion

---

## Problem Statement

Given the head of a linked list and a value, insert a new node at the **end (tail)** of the list.

**Example:**
```
Input:  1 → 2 → 3 → None,  val = 7
Output: 1 → 2 → 3 → 7 → None
```

---

## Approach — Traverse to Tail + Append

Traverse to the last node and attach the new node there.

```python
def insertAtEnd(head, x):
    new_node = Node(x)

    # Edge case: empty list
    if head is None:
        head = new_node
        return head

    # Traverse to the last node
    temp = head
    while temp.next != None:
        temp = temp.next

    # Attach new node at the end
    temp.next = new_node
    return head
```

**Visualization:**
```
Before: [1] → [2] → [3] → None
                             ↑ temp stops here (temp.next = None)

After:  [1] → [2] → [3] → [7] → None
```

---

## Why This Approach?

- In a singly linked list, there is no direct access to the tail — traversal is required
- **Optimization**: maintaining a `tail` pointer makes insertion `O(1)` — but that requires a full list class
- For the basic version, this is the simplest and clearest approach

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — must traverse to reach the tail |
| **Space** | `O(1)` — only one new node |

---

## Key Learning

> If frequent end insertions are needed, maintain a **tail pointer** in your class — reduces from `O(n)` to `O(1)`. This same concept is used in the `Queue` data structure (enqueue = insert at tail).
