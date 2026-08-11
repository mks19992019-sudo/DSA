# Merge Two Sorted Lists — My Approach and Mistakes

Problem: Merge two sorted singly linked lists into one sorted linked list.

Example:

```text
list1: 1 → 2 → 4
list2: 1 → 3 → 4

Output:
1 → 1 → 2 → 3 → 4 → 4
```

## 1. My Initial Approach

I wanted to solve the problem without creating any new `ListNode`.

My idea was:

1. Find the smaller first node and make it the `head`.
2. Compare the current nodes of both lists.
3. Connect the smaller node to the merged list.
4. Move that list's pointer forward.
5. Continue until one list becomes empty.
6. Attach the remaining list.

The first part was:

```python
if list1 is None:
    return list2

if list2 is None:
    return list1
```

This was correct.

If one list is empty, the other list can directly be returned.

---

## 2. Finding the Head

I first wrote:

```python
if list1.val >= list2.val:
    head = list2
else:
    head = list1
```

The idea was correct: choose the smaller first node.

It can be written more clearly as:

```python
if list1.val <= list2.val:
    head = list1
else:
    head = list2
```

But I made an important mistake here.

After selecting the head, I also needed to move that list's pointer forward.

Correct:

```python
if list1.val <= list2.val:
    head = list1
    list1 = list1.next
else:
    head = list2
    list2 = list2.next
```

Why?

If:

```text
list1: 1 → 2 → 4
list2: 1 → 3 → 4
```

and `1` from `list1` becomes the head, then `list1` must move to:

```text
list1: 2 → 4
```

Otherwise, I would process the same `1` again.

---

## 3. My First Attempt Using `temp`

I initially tried to solve it by saving the next node in a temporary variable:

```python
temp = list2.next
list2.next = list1
list2 = temp
```

or:

```python
temp = list1.next
list1.next = list2
list1 = temp
```

My thinking was that `temp` would preserve the next node before changing the pointer.

The idea of using `temp` was not necessarily wrong.

The actual problem was that I was modifying the `next` pointer of nodes that were already part of the merged list.

---

## 4. Main Mistake — I Was Not Tracking the Last Node

My code was doing things like:

```python
list2.next = list1
```

and:

```python
list1.next = list2
```

Consider:

```text
list1: 1 → 2 → 4
list2: 1 → 3 → 4
```

Suppose I do:

```python
list2.next = list1
```

Now:

```text
1(list2) → 1(list1) → 2 → 4
```

Then in the next iteration, I might do:

```python
list1.next = list2
```

Now the `next` pointer of that first `1` is overwritten.

Instead of:

```text
1 → 2
```

it becomes:

```text
1 → 3
```

So the `2` node gets disconnected from the merged chain.

This helped me identify the real issue:

> `temp` saves the next node, but I also need to know where the end of my merged list currently is.

---

## 5. Introducing `current`

To solve this, I introduced:

```python
current = head
```

Now I have two different responsibilities:

```text
head     → first node of the final merged list
current  → last node of the merged list
```

`head` should never move because I need it to return the final list.

`current` moves forward as I add nodes.

---

## 6. Correct Merging Logic

The loop becomes:

```python
while list1 and list2:

    if list1.val <= list2.val:
        current.next = list1
        list1 = list1.next
    else:
        current.next = list2
        list2 = list2.next

    current = current.next
```

Each iteration does three things.

First, compare:

```python
if list1.val <= list2.val:
```

Second, attach the smaller node:

```python
current.next = list1
```

Third, move the pointers:

```python
list1 = list1.next
current = current.next
```

The same logic applies to `list2`.

---

## 7. Another Mistake — Forgetting the Remaining List

The loop is:

```python
while list1 and list2:
```

This stops as soon as either list becomes empty.

For example:

```text
list1: 5 → 6
list2: empty
```

The nodes `5 → 6` are still remaining.

Because that list is already sorted, I can directly attach it:

```python
if list1:
    current.next = list1
else:
    current.next = list2
```

This is necessary to include the remaining nodes.

---

# Final Code — Without Dummy Node

```python
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # Find the first node
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head

        # Merge both lists
        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach the remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return head
```

## Mistakes I Found

```text
1. I selected the head but did not move the selected list pointer forward.

2. I was directly modifying list1.next and list2.next.

3. I used temp to save the next node, but I was not tracking
   the last node of the merged list.

4. I initially created current but did not actually use it
   to connect the nodes.

5. I forgot that after the while loop, one list can still
   contain remaining nodes.

6. The head must be decided only once.
   It should not be reassigned inside the while loop.
```

## Final Understanding

```text
head     → first node of the final answer
current  → last node of the merged list
list1    → current node of list1
list2    → current node of list2
```

The key idea I learned is:

> `head` stays fixed, `current` moves, and `list1`/`list2` are used to find the next smallest node.

## Complexity

```text
Time Complexity:  O(n + m)
Space Complexity: O(1)
```

No new `ListNode` is created. Only the existing nodes and their `next` pointers are rearranged.
