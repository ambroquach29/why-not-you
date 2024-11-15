# Why Not You?

> The Man in the Arena
>
> "It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows great enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph of high achievement, and who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat."
>
> — Theodore Roosevelt

My personal journey through computer science fundamentals, from data structures and algorithms to software engineering practices, with plans to explore data science, artificial intelligence, and machine learning. This repository serves as my learning playground and a collection of implementations that I'm building to understand the building blocks of modern computing.

## 🚀 My Learning Vision

This repository is organized as my progressive learning path covering:

### 📚 **1: Data Structures** (Current Focus)

- Complete implementations of fundamental data structures
- Interactive testing framework
- Performance analysis and complexity understanding

### 🔍 **2: Algorithms** (Coming Soon)

- Sorting algorithms (Bubble, Quick, Merge, Heap, etc.)
- Searching algorithms (Linear, Binary, Depth-First, Breadth-First)
- Graph algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall)
- Dynamic programming solutions
- Greedy algorithms
- Divide and conquer strategies

### 🏗️ **3: Software Engineering** (Planned)

- Design patterns and architectural principles
- Testing strategies (Unit, Integration, E2E)
- Code optimization and performance tuning
- System design and scalability
- API design and development
- Database design and optimization

### 🤖 **4: Data Science + AI + ML** (Future)

- Statistical analysis and data visualization
- Machine learning algorithms from scratch
- Deep learning implementations
- Natural language processing
- Computer vision basics
- Model evaluation and deployment

## 🎯 What I'm Building

- **Complete Data Structure Implementations**: From basic to advanced structures
- **Interactive Testing Framework**: Built-in test methods for each data structure
- **Educational Focus**: Well-documented code with clear explanations
- **Production-Ready Code**: Proper error handling and edge case management
- **Modular Design**: Each data structure is implemented as a separate, reusable class

## 📚 Implemented Data Structures

### Linear Data Structures

- **Singly Linked List** (`singly_linked_list.py`)

  - Add/remove at beginning and end
  - Insert/remove at specific positions
  - Search and traversal operations
  - O(1) head/tail operations, O(n) for arbitrary positions

- **Doubly Linked List** (`doubly_linked_list.py`)

  - Bidirectional traversal
  - Insert/delete at head, tail, and arbitrary positions
  - Forward and backward traversal methods
  - Enhanced search capabilities

- **Stack** (`custom_stack.py`)

  - LIFO (Last In, First Out) operations
  - Push, pop, and peek operations
  - Dynamic size management
  - O(1) time complexity for all operations

- **Queue** (`custom_queue.py`)

  - FIFO (First In, First Out) operations
  - Enqueue, dequeue, and peek operations
  - Efficient front-end operations
  - O(1) time complexity for enqueue/dequeue

- **Priority Queue** (`priority_queue.py`)
  - Priority-based element ordering
  - Customizable priority handling
  - Efficient priority management

### Tree Data Structures

- **Binary Tree** (`binary_tree.py`)

  - Complete tree implementation with comprehensive traversal methods
  - BFS (Breadth-First Search) and DFS (Depth-First Search)
  - Height and size calculations
  - Path finding from root to any node
  - Level-order traversal and conversion to list

- **Binary Search Tree** (`binary_search_tree.py`)

  - Ordered tree structure
  - Efficient search, insert, and delete operations
  - Inorder traversal for sorted output

- **Tree Node** (`tree_node.py`)
  - Flexible node structure for tree implementations
  - Support for left/right child pointers

### Advanced Data Structures

- **Hash Table** (`hash_table.py`)

  - Key-value pair storage
  - Efficient lookup and insertion
  - Collision handling

- **Trie** (`trie.py`)

  - Prefix tree for string operations
  - Efficient string search and storage

- **Min Heap** (`min_heap.py`)

  - Priority queue with minimum element at root
  - Efficient heap operations

- **Max Heap** (`max_heap.py`)

  - Priority queue with maximum element at root
  - Heap sort capabilities

- **Graph** (`graph.py`)
  - Graph representation and algorithms
  - Support for directed and undirected graphs

### Utility Classes

- **Node** (`node.py`)
  - Basic node structure for linked lists
  - Flexible element storage

## 🔮 My Roadmap

### Phase 2: Algorithms (Next Priority)

```
algorithms/
├── sorting/
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── heap_sort.py
│   └── insertion_sort.py
├── searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── depth_first_search.py
│   └── breadth_first_search.py
├── graph_algorithms/
│   ├── dijkstra.py
│   ├── bellman_ford.py
│   ├── floyd_warshall.py
│   └── topological_sort.py
├── dynamic_programming/
│   ├── fibonacci.py
│   ├── longest_common_subsequence.py
│   ├── knapsack.py
│   └── edit_distance.py
└── greedy/
    ├── activity_selection.py
    ├── huffman_coding.py
    └── kruskal_algorithm.py
```

### Phase 3: Software Engineering

```
software_engineering/
├── design_patterns/
│   ├── creational/
│   ├── structural/
│   └── behavioral/
├── testing/
│   ├── unit_tests/
│   ├── integration_tests/
│   └── performance_tests/
├── system_design/
│   ├── scalable_architectures/
│   ├── database_design/
│   └── api_design/
└── optimization/
    ├── code_optimization/
    ├── memory_management/
    └── performance_profiling/
```

### Phase 4: Data Science + AI + ML

```
data_science/
├── statistics/
│   ├── descriptive_statistics.py
│   ├── probability_distributions.py
│   └── hypothesis_testing.py
├── machine_learning/
│   ├── supervised_learning/
│   ├── unsupervised_learning/
│   └── reinforcement_learning/
├── deep_learning/
│   ├── neural_networks/
│   ├── cnn/
│   └── rnn/
└── data_visualization/
    ├── matplotlib_examples/
    ├── seaborn_examples/
    └── plotly_examples/
```

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher
- No external dependencies required (pure Python implementation)

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd why-not-you

# Navigate to data structures
cd data-structures

# Run the main testing program
python main.py
```

## 🧪 Usage Examples

### Running Tests

The project includes a comprehensive testing framework in `main.py`:

```python
from main import DS, switch_test_methods

# Test singly linked list
switch_test_methods(DS.SLL)

# Test binary tree
switch_test_methods(DS.BT)

# Test stack operations
switch_test_methods(DS.STACK)
```

### Individual Data Structure Usage

#### Singly Linked List

```python
from singly_linked_list import SinglyLinkedList

# Create and populate
sll = SinglyLinkedList()
sll.add_last(1)
sll.add_last(2)
sll.add_last(3)
sll.insert(5, 1)  # Insert 5 at index 1

print(sll)  # Visual representation
print(sll.remove_at_index(2))  # Remove element at index 2
```

#### Binary Tree

```python
from binary_tree import BinaryTree

# Create and populate tree
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

# Traversal methods
tree.inorder_traversal()
tree.level_order_traversal()

# Search operations
found = tree.bfs(5)  # Breadth-first search
path = tree.find_path_from_root(5)  # Find path from root to node
```

#### Stack

```python
from custom_stack import Stack

# Create stack with initial elements
stack = Stack([1, 2, 3, 4])
stack.push(5)
print(f'Top: {stack.peek()}')
print(f'Popped: {stack.pop()}')
```

## 📊 Performance Characteristics

| Data Structure     | Access       | Search       | Insertion                      | Deletion                       | Space |
| ------------------ | ------------ | ------------ | ------------------------------ | ------------------------------ | ----- |
| Singly Linked List | O(n)         | O(n)         | O(1) head/tail, O(n) arbitrary | O(1) head/tail, O(n) arbitrary | O(n)  |
| Doubly Linked List | O(n)         | O(n)         | O(1) head/tail, O(n) arbitrary | O(1) head/tail, O(n) arbitrary | O(n)  |
| Stack              | O(n)         | O(n)         | O(1)                           | O(1)                           | O(n)  |
| Queue              | O(n)         | O(n)         | O(1)                           | O(1)                           | O(n)  |
| Binary Tree        | O(n)         | O(n)         | O(n)                           | O(n)                           | O(n)  |
| Binary Search Tree | O(log n) avg | O(log n) avg | O(log n) avg                   | O(log n) avg                   | O(n)  |
| Hash Table         | O(1) avg     | O(1) avg     | O(1) avg                       | O(1) avg                       | O(n)  |

## 🎯 What I'm Learning

### 1: Data Structures

- **Data Structure Fundamentals**: Understanding how different data structures work
- **Algorithm Analysis**: Time and space complexity analysis
- **Python Programming**: Object-oriented programming, recursion, and advanced Python features
- **Problem-Solving Skills**: Implementing complex algorithms from scratch
- **Code Organization**: Modular design and clean code practices

### 2: Algorithms (Future)

- **Algorithm Design**: Understanding different algorithmic paradigms
- **Complexity Analysis**: Advanced time and space complexity analysis
- **Optimization Techniques**: Performance tuning and algorithm optimization
- **Problem-Solving Patterns**: Recognizing and applying algorithmic patterns

### 3: Software Engineering (Future)

- **System Design**: Scalable architecture and design principles
- **Testing Strategies**: Comprehensive testing methodologies
- **Code Quality**: Best practices for maintainable code
- **Performance Engineering**: Optimization and profiling techniques

### 4: Data Science + AI + ML (Future)

- **Statistical Analysis**: Understanding data and drawing insights
- **Machine Learning**: Implementing ML algorithms from scratch
- **Deep Learning**: Neural network architectures and training
- **Data Visualization**: Communicating insights through visualizations

## 🔧 Extending the Project

### Adding New Data Structures

1. Create a new Python file in the `data-structures/` directory
2. Implement your data structure class
3. Add it to the `DS` enum in `main.py`
4. Create a test method and add it to the switch statement

### Extending Existing Structures

Each data structure is designed to be easily extensible. You can:

- Add new methods to existing classes
- Implement additional traversal algorithms
- Add visualization capabilities
- Create specialized variants

## 🤝 Join the Journey

I'd love to have you join me on this learning adventure! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Implement your changes** with proper documentation
4. **Add tests** for new functionality
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

### Areas Where I'd Love Help

- **Data Structures**: Implement missing data structures or improve existing ones
- **Algorithms**: Add sorting, searching, or graph algorithms
- **Software Engineering**: Contribute design patterns or testing examples
- **Documentation**: Improve READMEs, add tutorials, or create learning guides
- **Performance**: Optimize existing implementations or add benchmarking

### Contribution Guidelines

- Follow existing code style and documentation patterns
- Add comprehensive docstrings for new methods
- Include usage examples in docstrings
- Update the main testing framework for new data structures
- Ensure all tests pass before submitting

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎓 Learning Resources

For deeper understanding, I'm exploring:

- **Algorithms**: Sorting, searching, and graph algorithms
- **Advanced Data Structures**: Red-black trees, B-trees, skip lists
- **Software Engineering**: Design patterns, testing strategies, code optimization
- **Machine Learning**: Data structures for ML algorithms
- **System Design**: Scalable data structure implementations

## 🆘 Getting Help

If you run into issues or have questions:

- Check the code comments and docstrings
- Review the test methods in `main.py` for usage examples
- Open an issue with detailed description of the problem
- Feel free to contribute improvements through pull requests

---

_Why not you? Start building, start learning, start growing._ 🚀
