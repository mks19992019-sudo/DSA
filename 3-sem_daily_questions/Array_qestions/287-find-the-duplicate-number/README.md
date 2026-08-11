# 287. Find the Duplicate Number

## Approach

Floyd's Cycle Detection

## Why I Used This Approach

I used Floyd's cycle method because the question asks for constant extra space. By treating values like pointers, we can find the duplicate without modifying the array.

## Time Complexity

`O(n)`

## Space Complexity

`O(1)`
