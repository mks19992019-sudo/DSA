# First Negative in Windows of Size K

## Approach

Sliding window with deque

## Why I Used This Approach

I used a deque to store useful negative indices only. This helps track the first negative element in each window without scanning the full window again.

## Time Complexity

`O(n)`

## Space Complexity

`O(k)`
