# 💡 Algorithms & Debugging – Summary Notes

---

## ⚙️ 1. Algorithmic Paradigms

| Type      | Description                            | Example              |
|-----------|----------------------------------------|----------------------|
| Brute-force | Try all possible solutions           | Subset sums, search  |
| Greedy      | Optimal at each step (local → global) | Activity selection   |
| Divide & Conquer | Break into sub-problems          | Merge Sort, QuickSort |
| Dynamic Programming | Reuse overlapping subproblems | Fibonacci, Knapsack  |

---

## 🔍 2. Search Algorithms

- **Linear Search**: O(n)
- **Binary Search**: O(log n), needs sorted data

---

## 🧪 3. Debugging Strategies

- Read the error trace!
- Use print-based tracing or IDE debuggers
- Binary search in code: isolate the bug scope

```python
# Python debug trick
import pdb; pdb.set_trace()
```

For C++, use gdb or valgrind for memory issues

## 🛠️ HackerRank Tips

- Check input/output formats carefully

- Test with corner cases

- Use fast I/O when needed (e.g., scanf, sys.stdin)

## Remember

- Algorithm correctness > optimization (initially)

- Practice recursion carefully (stack overflows possible)
