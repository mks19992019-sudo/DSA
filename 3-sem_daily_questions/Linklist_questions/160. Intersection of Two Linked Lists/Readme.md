# Intersection of Two Linked Lists

## Problem

Find the node where two singly linked lists intersect. If there is no intersection, return `None`.

## Approach — Hash Map

I store all nodes of `headA` in a hash map:

```python
hashMap[temp] = 1
```

Then I traverse `headB` and check whether each node already exists in the hash map.

```python
if temp in hashMap:
    return temp
```

I store the **node itself**, not its value, because intersection means both lists point to the **same node**, not just nodes having the same value.

## Complexity

```text
Time:  O(n + m)
Space: O(n)
```

## Key Learning

The important concept is that linked-list intersection is based on **node reference**, not node value.
