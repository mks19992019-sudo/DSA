# 📦 Arrays

> DSA 3rd Semester — Array Questions Collection

All array problems solved with detailed approach, time & space complexity analysis.

---

## 📊 Progress — `14 / 14` Solved

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1 | [Two Sum](./two-sum/) | 🟢 Easy | Hash Map | O(n) | O(n) |
| 2 | [66. Plus One](./66-plus-one/) | 🟢 Easy | Carry propagation | O(n) | O(1) |
| 3 | [Single Number](./single-number/) | 🟢 Easy | XOR Bit Trick | O(n) | O(1) |
| 4 | [Majority Element](./majority-element/) | 🟢 Easy | Boyer-Moore Voting | O(n) | O(1) |
| 5 | [349. Intersection of Two Arrays](./349-intersection-of-two-arrays/) | 🟢 Easy | Set Intersection | O(n+m) | O(n) |
| 6 | [Rotate Array by One](./rotate-array-by-one/) | 🟢 Easy | Save last, shift right | O(n) | O(1) |
| 7 | [189. Rotate Array](./189-rotate-array/) | 🟡 Medium | Triple Reverse | O(n) | O(1) |
| 8 | [53. Maximum Subarray](./53-maximum-subarray/) | 🟡 Medium | Kadane's Algorithm | O(n) | O(1) |
| 9 | [75. Sort Colors](./75-sort-colors/) | 🟡 Medium | Dutch National Flag | O(n) | O(1) |
| 10 | [287. Find the Duplicate Number](./287-find-the-duplicate-number/) | 🟡 Medium | Floyd's Cycle Detection | O(n) | O(1) |
| 11 | [2149. Rearrange Array Elements by Sign](./2149-rearrange-array-elements-by-sign/) | 🟡 Medium | Two-Pointer Placement | O(n) | O(n) |
| 12 | [1749. Maximum Absolute Sum of Any Subarray](./1749-maximum-absolute-sum-of-any-subarray/) | 🟡 Medium | Kadane's (max + min) | O(n) | O(1) |
| 13 | [239. Sliding Window Maximum](./239.%20Sliding%20Window%20Maximum/) | 🔴 Hard | Monotonic Deque | O(n) | O(k) |
| 14 | [First Negative in Windows of Size K](./first-negative-in-windows-of-size-k/) | 🟡 Medium | Sliding Window + Queue | O(n) | O(k) |

---

## 🗂️ Folder Structure

Each question folder contains:
```
<question-name>/
├── README.md       ← Approach, why I used it, TC/SC
└── solution.ipynb  ← Code + markdown explanation
```

---

## 🧠 Key Algorithms Covered

| Algorithm | Questions |
|---|---|
| **Kadane's Algorithm** | Max Subarray, Max Absolute Sum |
| **Hash Map** | Two Sum, Intersection |
| **Two Pointers** | Sort Colors (Dutch Flag), Rearrange by Sign |
| **Sliding Window** | Sliding Window Max, First Negative in Window |
| **XOR Trick** | Single Number |
| **Floyd's Cycle** | Find Duplicate |
| **Boyer-Moore Voting** | Majority Element |
