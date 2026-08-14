# Pairwise Swap in Linked List

> **Difficulty:** 🟡 Medium &nbsp;|&nbsp; **Topic:** Linked List — In-place Node Swapping

---

## Problem Statement

Given a singly linked list, swap every two adjacent nodes and return the head of the modified list. The swap must be done by **changing node links**, not by swapping values.

**Example:**
```
Input:  1 → 2 → 3 → 4 → 5
Output: 2 → 1 → 4 → 3 → 5

Input:  1 → 2 → 3 → 4
Output: 2 → 1 → 4 → 3
```

---

## Approach — Iterative Link Reversal with `prev`

Use three pointers: `first`, `sec`, and `prev`.
- `first` → the first node of the current pair
- `sec` → the second node of the current pair (gets placed before `first`)
- `prev` → the last node of the already-swapped portion (used to link back)

```python
def pairwiseSwap(head):
    first = head
    sec = head.next
    prev = None

    # Edge case: empty list or single node
    if head == None or head.next == None:
        return head

    while sec != None:
        third = sec.next    # save the rest of the list

        # Perform the swap
        sec.next = first
        first.next = third

        # Link the previous pair to the new head of this pair
        if prev != None:
            prev.next = sec
        else:
            head = sec      # first pair: update the new head

        prev = first        # first becomes the tail of this pair

        # Advance to next pair
        first = third

        if third != None:
            sec = third.next
        else:
            return head

    return head
```

**Step-by-step on `1 → 2 → 3 → 4`:**
```
Initial:
first=1, sec=2, prev=None

Iteration 1:
  third = 3
  sec.next = first  →  2 → 1
  first.next = third → 1 → 3
  prev is None → head = sec = 2
  prev = first = 1
  first = 3, sec = 4

  List so far: 2 → 1 → 3 → 4

Iteration 2:
  third = None
  sec.next = first  →  4 → 3
  first.next = third → 3 → None
  prev.next = sec   →  1 → 4
  prev = first = 3
  first = None → return head

  Final: 2 → 1 → 4 → 3 ✓
```

---

## Why This Approach?

- Swaps are done by **relinking nodes**, not swapping values — this is the required approach for linked list node swap problems
- `prev` pointer is essential to connect the previous swapped pair to the current one
- The `head` update only happens once (for the first pair) — after that, `prev.next = sec` handles all connections

---

## Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — every node is visited exactly once |
| **Space** | `O(1)` — in-place relinking, no extra memory |

---

## Key Learning

> In pairwise swapping, you need **three pointers** (`first`, `sec`, `prev`) and must be careful to save `sec.next` before modifying any links — otherwise the rest of the list is lost. The new head is always `sec` of the very first pair.
