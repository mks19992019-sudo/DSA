# Check If Linked List is Circular

> **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Topic:** Linked List — Cycle Detection

---

## Problem Statement

Given the head of a linked list, determine whether it contains a **cycle** (i.e., some node's `.next` points back to a previous node in the list).

**Example:**
```
Circular:     1 → 2 → 3 → 4
                        ↑       |
                        └───────┘

Not Circular: 1 → 2 → 3 → None
```

---

## Approach — Floyd's Cycle Detection (Tortoise & Hare)

Do pointers use karte hain:
- **Slow pointer** (`tortoise`) — ek step at a time
- **Fast pointer** (`hare`) — do steps at a time

```python
def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps

        if slow == fast:        # they met — cycle exists!
            return True

    return False  # fast reached end — no cycle
```

**Why do they meet?**
> Agar cycle hai, toh fast pointer cycle mein ghoomta rehta hai. Slow poochter bhi cycle mein aa jaata hai. Ab dono ek hi loop mein hain aur fast slow se har iteration mein 1 step aage badhta hai — toh eventually dono milenge!

---

## Why This Approach?

- **Visited set** alternative: `O(n)` space use hota hai (har node ko set mein daalo)
- **Floyd's algorithm** sirf `O(1)` extra space use karta hai — **best approach**
- Industry-standard algorithm hai cycle detection ke liye

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — fast pointer poori list traverse karega max |
| **Space** | `O(1)` — sirf 2 pointers |

---

## Key Learning

> Floyd's Cycle Detection ek **two-pointer classic** hai. Cycle se related koi bhi question dekho — yahi pehla sochna chahiye. Yeh linked list mein **cycle start dhundne** (LeetCode 142) ke liye bhi extend hota hai.
