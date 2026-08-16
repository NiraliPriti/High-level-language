# Java-Basics

# Java Data Structures & Algorithms (DSA) Masterclass

A production-grade repository documenting my journey through advanced Data Structures, Algorithms, and Technical Interview Preparation. This repository showcases clean Java architecture, robust Object-Oriented design patterns, optimized Big-O complexity, and rigorous edge-case handling.

---

## 🛠️ Repository Architecture

Problems are organized logically by foundational computer science categories. Every solution is written natively in Java.

```text
📁 java-dsa-masterclass/
├── 📁 data_structures/     # Custom implementations and problem sets (Arrays, Trees, Graphs, Lists)
├── 📁 algorithms/          # Algorithmic strategies (Recursion, Sorting, DP, Greedy)
├── 📁 concurrency/         # Java-specific multi-threading and synchronization interview concepts
└── 📄 README.md            # Repository Strategy & Dynamic Progress Tracker
```

---

## 📊 Progress Dashboard

| Topic | Problem Name | LeetCode # | Core Java Implementation | Complexity | Difficulty |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Arrays** | Two Sum | 1 | [TwoSum.java](#) | $O(N)$ Time / $O(N)$ Space | 🟢 Easy |
| **Arrays** | Container With Most Water | 11 | [ContainerWater.java](#) | $O(N)$ Time / $O(1)$ Space | 🟡 Medium |
| **Linked List** | Reverse Linked List | 206 | [ReverseList.java](#) | $O(N)$ Time / $O(1)$ Space | 🟢 Easy |
| **Strings** | Longest Substring Without Repeating Chars | 3 | [LongestSubstring.java](#) | $O(N)$ Time / $O(K)$ Space | 🟡 Medium |
| **Trees** | Maximum Depth of Binary Tree | 104 | [MaxDepthBinaryTree.java](#) | $O(N)$ Time / $O(H)$ Space | 🟢 Easy |

---

## 💡 Code Standard & Production Rigour

To reflect enterprise-level standards, every Java class file in this repository strictly adheres to these rules:

1. **Iterative Optimization:** Files include both an initial naive approach (commented out) and a fully optimized, production-ready version to showcase iterative technical reasoning.
2. **Explicit Complexity Analysis:** Big-O Time and Space complexities are explicitly documented in the Javadoc header of every class.
3. **Type Safety & Generics:** Data structures leverage Java Generics (`<T>`) where applicable to ensure robust compile-time type safety.
4. **Self-Contained Runner:** Every solution file contains an executable `public static void main(String[] args)` block containing at least three test cases explicitly validating boundary bounds and negative edge cases.

---

## 🎯 Core Technical Focus
*   **Java Collections Framework:** Mastering deep optimization of `ArrayList`, `HashMap`, `PriorityQueue`, and `HashSet`.
*   **Memory Efficiency:** Understanding the memory footprints of primitive types (`int`, `char`) versus wrapper objects (`Integer`, `Character`) during scaling.
