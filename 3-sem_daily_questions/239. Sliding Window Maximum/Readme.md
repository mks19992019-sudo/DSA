# 239. Sliding Window Maximum

**Difficulty:** Hard
**Topic:** Array, Sliding Window, Deque, Monotonic Queue
**LeetCode:** 239

## Problem

Given an array `nums` and a window of size `k`, find the maximum element in every sliding window.

## Example

```text
Input:
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:
[3,3,5,5,6,7]
```

## Approach

Use a **Monotonic Decreasing Deque**.

The deque stores **indices**, not values.

For every index `i`:

* Remove indices from the back whose values are smaller than `nums[i]`.
* Add the current index to the deque.
* Once the window reaches size `k`, the front of the deque contains the maximum element.
* Remove the index from the front if it has gone outside the current window.

## Code

```python
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        q = deque()

        for i in range(len(nums)):

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                ans.append(nums[q[0]])

            if q and (i - k + 1) == q[0]:
                q.popleft()

        return ans
```

## Why Deque?

The deque maintains elements in decreasing order of their values:

```text
nums[q[0]] >= nums[q[1]] >= nums[q[2]] ...
```

Therefore:

```python
nums[q[0]]
```

is always the maximum element of the current window.

## Complexity

**Time Complexity:** `O(n)`

Every index is added to the deque once and removed from the deque at most once.

**Space Complexity:** `O(k)`

The deque stores at most `k` indices.

## Key Pattern

**Sliding Window + Monotonic Deque**

This pattern is useful for:

* Maximum/Minimum in a sliding window
* Monotonic queues
* Next greater/smaller element problems
* Efficient range queries

## Core Logic

```text
Current element is bigger
        ↓
Remove smaller elements from the back
        ↓
Add current index
        ↓
Window size becomes k
        ↓
Deque front = maximum
        ↓
Remove expired index
```

## Important Insight

The deque does **not** store all elements of the window.

It stores only the indices that can potentially become the maximum.

If a new element is greater than an element at the back of the deque, that older element can never become the maximum of any future window containing the new element, so it is removed.
