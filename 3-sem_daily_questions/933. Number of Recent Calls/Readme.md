

# 933. Number of Recent Calls

**Difficulty:** Easy
**Topic:** Queue, Sliding Window
**LeetCode:** 933

## Problem

Count how many requests occurred within the last `3000` milliseconds for each `ping(t)`.

## Approach

Use a **Deque** to maintain timestamps within the current time window.

For every new timestamp:

* Add the new timestamp.
* Remove timestamps older than `t - 3000`.
* The deque size gives the number of recent requests.

## Complexity

**Time:** `O(1)` amortized per call
**Space:** `O(n)`



