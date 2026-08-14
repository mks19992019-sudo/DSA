# 160. Intersection of Two Linked Lists

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; **LeetCode:** [#160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

---

## Problem Statement

Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If the two lists have no intersection, return `null`.

> Intersection means both lists share the **same node object** (by reference), not just the same value.

**Example:**
```
listA:  a1 → a2 ↘
                  c1 → c2 → c3
listB:  b1 → b2 ↗

Intersection node: c1
```

---

## Approach 1 — HashMap

Store all nodes of `headA` in a hash map. Then traverse `headB` and check if each node already exists in the map.

```python
def getIntersectionNode(headA, headB):
    hashMap = {}
    temp = headA

    # Store every node of listA
    while temp:
        hashMap[temp] = 1
        temp = temp.next

    # Check every node of listB
    temp = headB
    while temp:
        if temp in hashMap:
            return temp     # intersection found
        temp = temp.next

    return None
```

> **Why store the node itself (not its value)?**
> Intersection is defined by **same node reference**, not same value. Two different nodes can have the same value but different addresses.

**Complexity:**

| | Complexity |
|---|---|
| **Time** | `O(n + m)` — traverse both lists once |
| **Space** | `O(n)` — hash map stores all nodes of listA |

---

## Approach 2 — Two Pointer (Linked List Method)

Use two pointers `t1` and `t2` starting at `headA` and `headB`. When either pointer reaches `None`, redirect it to the other list's head. They will meet at the intersection node (or both reach `None` if no intersection).

```python
def getIntersectionNode(headA, headB):
    if headA == None or headB == None:
        return None

    t1 = headA
    t2 = headB

    while t1 != t2:
        t1 = t1.next
        t2 = t2.next

        if t1 == t2:
            return t1

        if t1 == None:
            t1 = headB
        if t2 == None:
            t2 = headA

    return t1
```

**Why does this work?**
```
listA length = a + c
listB length = b + c   (c = shared tail length)

t1 travels: a + c + b steps to reach intersection
t2 travels: b + c + a steps to reach intersection
→ Both travel the same total distance → they meet!
```

**Complexity:**

| | Complexity |
|---|---|
| **Time** | `O(n + m)` — both pointers traverse at most both lists |
| **Space** | `O(1)` — no extra memory |

---

## Key Learning

> Linked list intersection is based on **node reference equality**, not value equality. The two-pointer trick works because both pointers cover the same total distance — eliminating the length difference between the two lists.
