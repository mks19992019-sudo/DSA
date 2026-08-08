# 232. Implement Queue using Stacks

## Approach

Two-stack queue simulation

## Why I Used This Approach

I used two stacks so I could preserve queue order while still using only stack operations. The optimized version transfers elements only when needed.

## Time Complexity

`Push: O(1), Pop/Peek: amortized O(1)`

## Space Complexity

`O(n)`
