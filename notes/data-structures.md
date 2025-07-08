# 📚 Data Structures – Summary Notes

This section consolidates key data structures assessed in the HackerRank Software Engineer Certificate.

---

## 📦 1. Arrays and Lists

- Fixed-size vs dynamic arrays
- Common ops: insert, delete, search (O(1)/O(n))
- Python: `list`, `deque` (from `collections`)
- C++: `vector`, `array`, `list`

---

## 🔄 2. Stacks and Queues

| Structure | Use Case                   | Language Example    |
|----------|----------------------------|---------------------|
| Stack    | Undo, backtracking, DFS    | `stack` (C++), `list[::-1]` (Python) |
| Queue    | Scheduling, BFS            | `queue` / `deque`   |

---

## 🌳 3. Trees and Graphs

- **Binary Trees** – recursive traversal (inorder, preorder, postorder)
- **BSTs** – efficient search/insert/delete (O(log n))
- **Graphs** – represented via adjacency list or matrix

> DFS and BFS are essential traversal algorithms

---

## 🗂️ 4. Hashing

- Fast lookup (O(1) average case)
- Python: `dict`, `set`
- C++: `unordered_map`, `unordered_set`

---

## 📐 5. Heaps and Priority Queues

- Min/Max heaps for optimal selection problems
- Used in Dijkstra, Huffman coding, etc.
- Python: `heapq`, C++: `priority_queue`

---

## ✅ Practice Tips

- Always consider time/space trade-offs
- Use dry runs and complexity analysis
- Optimize for worst-case scenarios

