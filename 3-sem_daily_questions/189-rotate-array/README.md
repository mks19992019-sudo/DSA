# 189. Rotate Array

## Approach

Array slicing with modulo adjustment

## Why I Used This Approach

I used slicing because it makes the rotation logic short and easy to understand. First I reduce `k` with modulo, then I place the last `k` elements in front.

## Time Complexity

`O(n)`

## Space Complexity

`O(n)`
