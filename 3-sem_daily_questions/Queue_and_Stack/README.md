# 📚 Queue and Stack

> DSA 3rd Semester — Queue & Stack Questions Collection

All queue and stack problems solved with detailed approach, diagrams, and complexity analysis.

---

## 📊 Progress — `4 / 4` Solved

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1 | [20. Valid Parentheses](./20-valid-parentheses/) | 🟢 Easy | Stack — push/pop matching | O(n) | O(n) |
| 2 | [232. Implement Queue Using Stacks](./232-implement-queue-using-stacks/) | 🟢 Easy | Two-stack flip trick | O(1) amortized | O(n) |
| 3 | [225. Implement Stack Using Queues](./225-implement-stack-using-queues/) | 🟢 Easy | Single queue rotate | O(n) push | O(n) |
| 4 | [933. Number of Recent Calls](./933.%20Number%20of%20Recent%20Calls/) | 🟢 Easy | Queue sliding window | O(1) avg | O(1) |

---

## 🗂️ Folder Structure

Each question folder contains:
```
<question-name>/
├── README.md       ← Approach, why I used it, TC/SC
└── solution.ipynb  ← Code + markdown explanation
```

---

## 🧠 Key Concepts Covered

| Concept | Questions |
|---|---|
| **Stack — Push/Pop** | Valid Parentheses, Implement Stack Using Queue |
| **Queue — FIFO** | Number of Recent Calls, Implement Queue Using Stacks |
| **Two-Stack Trick** | Implement Queue Using Stacks |
| **Sliding Window with Queue** | Number of Recent Calls |

---

## 📌 Stack vs Queue — Quick Recap

| | Stack | Queue |
|---|---|---|
| **Order** | LIFO (Last In First Out) | FIFO (First In First Out) |
| **Insert** | `push` (top) | `enqueue` (rear) |
| **Remove** | `pop` (top) | `dequeue` (front) |
| **Use Case** | Undo, recursion, parentheses | BFS, scheduling, recent calls |
