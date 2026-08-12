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

Tail tak traverse karo aur naya node wahan attach karo.

```python
def insert_at_end(head, val):
    new_node = Node(val)

    # Edge case: empty list
    if head is None:
        return new_node

    # Traverse to the last node
    curr = head
    while curr.next:
        curr = curr.next

    # Attach new node at the end
    curr.next = new_node
    return head
```

**Visualization:**
```
Before: [1] → [2] → [3] → None
                            ↑ curr stops here (curr.next = None)

After:  [1] → [2] → [3] → [7] → None
```

---

## Why This Approach?

- Singly linked list mein tail ka direct access nahi hota — traverse karna padta hai
- **Optimization**: `tail` pointer maintain karo toh insertion `O(1)` ho jaaye — lekin tab poori list class banana padti hai
- Basic version mein yeh simplest aur clearest approach hai

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — tail tak traverse karna padta hai |
| **Space** | `O(1)` — sirf ek naya node |

---

## Key Learning

> Agar baar baar end insertion chahiye, toh **tail pointer** maintain karo in your class — `O(n)` se `O(1)` ho jaayega. Yahi concept `Queue` data structure mein use hota hai (enqueue = insert at tail).
