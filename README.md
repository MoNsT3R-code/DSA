# Data Structures & Algorithms (DSA) Engine

An object-oriented, performance-optimized suite of core data structures, self-balancing trees, graph traversal algorithms, and abstract data types built from scratch in Python.

![Language](https://img.shields.io/badge/Language-Python%203.x-blue?logo=python&logoColor=white)
![Data Engine](https://img.shields.io/badge/Data%20Engine-Custom%20Memory%20ADTs-orange?logo=databricks&logoColor=white)
![Design Pattern](https://img.shields.io/badge/Pattern-Object--Oriented%20%28OOP%29-green)
![Interface](https://img.shields.io/badge/Interface-Console%20Terminal-lightgrey)

---

## 🌐 Engine Overview

The DSA Engine serves as a comprehensive, production-grade practice workspace. By decoupling raw memory allocation emulation (such as static array tracking in custom `DynamicArray` classes) from hierarchical tree balancing and graph traversal threads, this repository provides complete visibility into low-level execution paths, runtime complexities ($\mathcal{O}$), and rigorous pointer manipulation models.

---

## 📍 Quick Navigation

* [🌐 Engine Overview](https://www.google.com/search?q=%23-engine-overview)
* [📦 System Architecture](https://www.google.com/search?q=%23-system-architecture)
* [📁 Repository Structure and Module Index](https://www.google.com/search?q=%23-repository-structure-and-module-index)
* [🛠️ Tech Stack & Requirements](https://www.google.com/search?q=%23%25EF%25B8%258F-tech-stack)
* [🚀 Setup & Execution Guide](https://www.google.com/search?q=%23-setup--execution-guide)
* [📊 Application Core Interfaces (Complexity Matrix)](https://www.google.com/search?q=%23-application-core-interfaces)
* [🏗️ Architectural & Algorithmic Highlights](https://www.google.com/search?q=%23-architectural--highlights)
* [🐛 Integrity & Diagnostics System](https://www.google.com/search?q=%23-integrity--diagnostics-system)

---

## 📦 System Architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│                  TOPOLOGICAL GRAPH & TREE LAYER                  │
├──────────────────────────────────────────────────────────────────┤
│          BFS Graph Traversals  │  AVL Tree Rotations             │
│          Adjacency Configurations │ Balanced Height Restructuring│
└──────────────────────────────┬───────────────────────────────────┘
                               ↓
┌──────────────────────────────────────────────────────────────────┐
│                ABSTRACT DATA TYPE (ADT) ENGINES                  │
├────────────┬─────────────┬────────────┬─────────────┬────────────┤
│ Binary Tree│ Min-Heap    │ Linear/    │ Stack &     │ Custom     │
│ Traversal  │ Priority    │ Log/Exp    │ Queue       │ SLL &      │
│ Sequences  │ Queues      │ Recursion  │ Controllers │ DLLs       │
└────────────┴─────────────┴────────────┴─────────────┴────────────┘
                               ↓
┌──────────────────────────────────────────────────────────────────┐
│                    FOUNDATIONAL COMPONENT LAYER                  │
├──────────────────────────────────────────────────────────────────┤
│         Dynamic Memory Arrays  │  Object-Oriented Schemas        │
└──────────────────────────────────────────────────────────────────┘

```

| Architectural Layer | Core Components & Strategies | Quick Links / Reference |
| --- | --- | --- |
| **Top: Advanced Relations** | Tree Balancing, Left/Right Rotations, and Graph Neighborhood Mapping | [Advanced Data Structures](https://www.google.com/search?q=%23-repository-structure-and-module-index) |
| **Middle: ADT Engines** | Specialized data layout classes featuring index mathematics and pointer shifts | [Repository Structure](https://www.google.com/search?q=%23-repository-structure-and-module-index) |
| **Bottom: Foundational** | Object inheritance structures and amortized growth-bound array buffers | [Complexity Matrix](https://www.google.com/search?q=%23-application-core-interfaces) |

### ✨ Key Architecture Features

* **Balanced Tree Architectures** – Implements a production-grade **AVL Tree** featuring automatic node rebalancing via localized pointer pivoting (`_left_rotate`, `_right_rotate`).
* **Stochastic Heap Bubble Inversions** – Employs element bubble structures (`upheap`/`downheap`) mapped entirely onto structural index equations to guarantee swift priority queue execution paths.
* **Two-Pointer Singly Linked List Parsing** – Leverages fast and slow index bounds to determine sub-sequence properties like node midpoints in a single linear sweep.
* **Amortized Dynamic Memory Management** – Minimizes standard allocation spikes by deploying geometric array doubling factors once base capacities are reached.

---

## 📁 Repository Structure and Module Index

The workspace organizes algorithmic files and code structures into standalone, executable scripts:

### 🐍 Production Python System Engines

* **`Assignment 2 DSA.py`** – High-end AVL tree application managing localized match profiles, implementing parent-node adjustments alongside functional sequential disk serialization.
* **`Lab 8 dsa.py`** – Unweighted bidirectional graph environment executing classic Breadth-First Searches (BFS) through standard collections queue trackers.
* **`Lab 7 dsa (1).py`** – Array-backed Min-Heap architecture mapping priority-queue bindings, index arithmetic, and systematic tree validations.
* **`Lab 7 DSA.py`** – Complexity research module breaking down recursion trees alongside explicit Stack and Queue templates running on custom internal arrays.
* **`lab 6 dsa.py`** – Standard Binary Search Tree (BST) layout handling multi-mode node sorting layouts (Inorder, Preorder, Postorder) and conditional leaf pruning blocks.
* **`lab 5 DSA.py`** – Doubly Linked List (DLL) processing hub containing reference mutations for handling sequential item insertion, removal, and complete index reversals.
* **`lab 4.py`** – Singly Linked List engine verifying positional pointer edits (`insert_after`, `insert_before`) alongside fast/slow mid-node identification algorithms.
* **`Lab 2 dsa.py`** – Base storage playground simulating custom dynamic sequence resizing, error bounds handling, and internal object comparisons.
* **`Lab 1 DSA.py`** – Foundational academic workspace exploring Object-Oriented paradigms (Inheritance, Overriding) alongside mathematical code run-time derivations.
* **`dsa.py` / `DSA practice.py` / `Assignment # 1_2 DSA.py**` – Core application scratchpads evaluating algorithmic scenarios, string data configurations, and balance filters.

### 🗃️ External Reference Metadata

* **`practice questions summer 2025 dsa.docx`** – Comprehensive external specifications directory tracking sample data structures scenarios and problem configurations.

---

## 🛠️ Tech Stack

| Component | Technology | Quick Links |
| --- | --- | --- |
| **Core Ecosystem** | Python 3.x Native Implementation Runtime | [python.org](https://www.google.com/search?q=https://python.org) |
| **Queue Pipelines** | Standard Double-Ended Array Node Trackers (`collections.deque`) | [docs.python.org/3/library/collections](https://www.google.com/search?q=https://docs.python.org/3/library/collections.html) |
| **Chronology Processing** | High-resolution profile timestamp tracking (`datetime`) | [docs.python.org/3/library/datetime](https://www.google.com/search?q=https://docs.python.org/3/library/datetime.html) |

### 💻 System Requirements

* **Interpreter Version:** Standard Python 3.x environment installed over the local running terminal shell.
* **Disk Constraints:** Unrestricted file system write access in the current execution folder to accommodate AVL data serialization (`matches.txt`).
* **Environment Configuration:** Clean, text-based interactive terminal window with console print outputs enabled.

---

## 🚀 Setup & Execution Guide

### Step 1: Clone the Repository Workspace

Pull down the directory workspace and transition into the primary execution environment:

```bash
git clone https://github.com/MoNsT3R-code/DSA.git
cd DSA

```

### Step 2: Running Algorithmic Execution Tracks

All modules operate as independent runtimes containing embedded validation drivers. For instance, to test the AVL Tree balancing engine and export its serialized document tree, run:

```bash
python "Assignment 2 DSA.py"

```

To run the Breadth-First Search graph traversal track:

```bash
python "Lab 8 dsa.py"

```

---

## 📊 Application Core Interfaces

Operational costs and runtimes map explicitly across these internal structural assets:

| Data Structure Category | Storage Blueprint Profile | Functional Operational Dependency | Average Algorithmic Time Complexity |
| --- | --- | --- | --- |
| **Dynamic Array** | Contiguous index blocks allocated sequentially in system memory. | Tracks variable item counts; triggers automatic doubling allocations when standard thresholds peak. | $$\text{Access: } \mathcal{O}(1)$$

<br>

<br>$$\text{Insertion: } \mathcal{O}(1) \text{ (Amortized)}$$

 |
| **Linked Lists (SLL/DLL)** | Decoupled pointer nodes wrapping custom value properties and memory handles. | Modifies front/end data tracks sequentially via reference overrides without complete layout updates. | $$\text{Search: } \mathcal{O}(n)$$

<br>

<br>$$\text{Insertion/Deletion: } \mathcal{O}(1)$$

 |
| **Binary Search Tree** | Hierarchical node branching linking parent values to left/right variations. | Maintained via strict data inequalities to handle optimized value lookups and deletions. | $$\text{Search/Insert/Delete: } \mathcal{O}(\log n)$$

<br> *(Average Case)* |
| **AVL Tree** | Self-balancing tree node matrices extending standard BST logic with height markers. | Actively tracks subtree height weights; triggers defensive rotation steps to prevent deep skewing. | $$\text{Search/Insert/Delete: } \mathcal{O}(\log n)$$

<br> *(Guaranteed)* |
| **Min-Heap (Priority Queue)** | Flattened index tree mapped onto a dense array. | Evaluates tree node balances; shifts properties via sequential swaps to keep optimal nodes at root level. | $$\text{Enqueue/Dequeue: } \mathcal{O}(\log n)$$

<br>

<br>$$\text{Peek Min: } \mathcal{O}(1)$$

 |

---

## 🏗️ Architectural Highlights

### 🎯 Rotational Balanced Balancing Constraints

The self-balancing module limits tree skewing by analyzing the balance factor ($BF$) at any node $N$, defined by the height variance between its left and right subtrees:

$$BF(N) = \text{height}(\text{node.left}) - \text{height}(\text{node.right})$$

A rotation event triggers if $|BF(N)| > 1$. The system then applies precision pivot mutations to restore structural equilibrium:

```text
       [z] (Unbalanced)               [y] (Balanced)
      /                              /   \
    [y]            ───►            [x]   [z]
   /   \                                /
 [x]   [T3]                           [T3]
 (Right Rotation applied to node z)

```

### 🧮 Amortized Dynamic Ingestion Formulas

To limit operational performance degradation across growing data streams, custom collection structures allocate supplementary storage buffers ahead of standard requirements:

$$\text{Capacity}_{\text{new}} = \text{Capacity}_{\text{current}} \times 2$$

This guarantees that while a resize step scales at a linear cost of $\mathcal{O}(n)$ to transfer items, the foundational build step over sequential insertions runs at a safe amortized rate of $\mathcal{O}(1)$.

---

## 🐛 Integrity & Diagnostics System

To maintain absolute system safety, this repository includes an internal verification registry detailing existing design bugs and their corresponding resolutions.

### 📝 The Bugs and Fixes Ledger

Refer to the dedicated **`The Bugs and Fixes`** file in your repository for structural diagnostics. Below is a tracking log of ongoing corrections required for production-ready cross-compilation:

* **Conditional Loop Overrides (`Lab 2 dsa.py`)**:
* *Bug:* Line 26 implements `if index < 0 or index >= 0:`, creating a tautology that completely locks the array mutation interface by always returning an error.
* *Fix:* Convert the logic block to use valid parameter thresholds: `if index < 0 or index >= self.size:`.


* **Casing Reference Typos (`lab 6 dsa.py`)**:
* *Bug:* Line 40 attempts to initialize a node utilizing `Parent.right = Parent(value)`, which accidentally triggers a class type name assignment instead of a structural pointer modification on the current node variable.
* *Fix:* Correct the capitalization to modify the intended local method variable: `parent.right = Parent(value)`.


* **Execution Pointer Extraction (`Lab 7 dsa (1).py`)**:
* *Bug:* Line 20 extracts a value via `return self.heap.pop`, which returns the underlying method address reference rather than running the internal pop routine.
* *Fix:* Append trailing operational indicators to execute the block properly: `return self.heap.pop()`.



---

## 📄 License & Terms

This algorithm suite is open-source. Feel free to copy, modify, adapt, or redistribute the data models and execution scripts for academic or architectural systems deployment.
