# 21. Merge Two Sorted Lists

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; **LeetCode:** [#21](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## Problem Statement

Given the heads of two sorted singly linked lists, merge them into one sorted linked list and return its head.

**Example:**
```
list1:  1 → 2 → 4
list2:  1 → 3 → 4

Output: 1 → 1 → 2 → 3 → 4 → 4
```

---

## Approach — Dummy Node + Iterative Merge

Create a dummy `new_node` as the starting anchor. Use a `current` pointer to build the merged list by always picking the smaller node from `list1` or `list2`.

```python
def mergeTwoLists(list1, list2):
    new_node = ListNode()   # dummy head node
    current = new_node

    while list1 and list2:
        if list1.val >= list2.val:
            current.next = list2
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next
        current = current.next

    # Attach whichever list still has remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2

    return new_node.next    # skip the dummy node
```

**Visualization:**
```
list1: 1 → 2 → 4
list2: 1 → 3 → 4

dummy →  ?
         ↑ current

Step 1: list2.val(1) <= list1.val(1) → attach list2's 1
dummy → 1(L2) → ?    current moves forward, list2 = 3→4

Step 2: list1.val(1) < list2.val(3) → attach list1's 1
dummy → 1 → 1(L1) → ?    current moves forward, list1 = 2→4

Step 3: list1.val(2) < list2.val(3) → attach list1's 2
...and so on

Final: dummy → 1 → 1 → 2 → 3 → 4 → 4
Return: new_node.next  (skip dummy)
```

---

## Why the Dummy Node?

- Without a dummy node, you have to handle "what is the first node of the merged list?" as a separate edge case
- With `new_node` as an anchor, `current` can always do `current.next = ...` without worrying about setting the head
- At the end, `new_node.next` is the real head of the merged list

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n + m)` — each node is visited exactly once |
| **Space** | `O(1)` — only one dummy node created, no extra memory for the list |

---

## Key Learning

> The **dummy node trick** eliminates head-selection edge cases. Instead of separately deciding which node is the head, let `current` build the entire list and return `dummy.next` at the end. After the while loop, **always attach the remaining list** directly — it is already sorted.
