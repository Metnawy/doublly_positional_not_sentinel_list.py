
# Doubly Linked List without Sentinel Nodes

This Python script implements a **Doubly Linked List** without using sentinel nodes. The list allows for efficient insertion, deletion, and traversal of elements in both forward and backward directions. The list is designed to provide positional access to nodes, enabling operations like adding, deleting, and swapping elements at specific positions.

## Features

- **Doubly Linked List**: Each node contains references to both the next and previous nodes, allowing for bidirectional traversal.
- **Positional Access**: Nodes are accessed via `_position` objects, which act as handles to specific nodes in the list.
- **Basic Operations**:
  - **Add/Remove Elements**: Add or remove elements at the beginning, end, or any specific position in the list.
  - **Swap Nodes**: Swap the values or positions of two nodes in the list.
  - **Sorting**: Sort the list in ascending or descending order.
  - **Iteration**: Iterate through the list using Python's `__iter__` method.
  - **Reversing**: Reverse the order of elements in the list.
- **Advanced Operations**:
  - **Merge Lists**: Merge two lists with or without modifying the original lists.
  - **Positional Manipulation**: Add, delete, or swap nodes based on their positions.

## Usage

### Initialization

To create a new doubly linked list:

```python
x = doublly_positional_not_sentinel_list()
```

### Adding Elements

- **Add to the beginning**:
  ```python
  x.add_first(10)
  ```
- **Add to the end**:
  ```python
  x.add_last(20)
  ```
- **Add at a specific position**:
  ```python
  pos = x.first_positon()  # Get the first position
  x.add_at_position(pos, 15)  # Add 15 at the first position
  ```

### Removing Elements

- **Remove the first element**:
  ```python
  x.delete_first()
  ```
- **Remove the last element**:
  ```python
  x.delete_last()
  ```
- **Remove a specific element**:
  ```python
  pos = x.first_positon()  # Get the first position
  x.delete_at_position(pos)  # Delete the first element
  ```

### Swapping Nodes

- **Swap values of two nodes**:
  ```python
  pos1 = x.first_positon()
  pos2 = x.last_position()
  x.swap_data_at_positions(pos1, pos2)
  ```
- **Swap nodes themselves**:
  ```python
  x.swap_nodes(pos1, pos2)
  ```

### Sorting

- **Sort in ascending order**:
  ```python
  sorted_list = x.ordering_asending()
  ```
- **Sort in descending order**:
  ```python
  sorted_list = x.ordering_desending()
  ```

### Iteration

- **Iterate through the list**:
  ```python
  for node in x:
      print(node.data)
  ```

### Reversing the List

- **Reverse the list**:
  ```python
  reversed_list = x.reverse()
  ```

### Merging Lists

- **Merge two lists with changes**:
  ```python
  y = doublly_positional_not_sentinel_list()
  y.add_first(30)
  x.merge_with_changes(y)
  ```
- **Merge two lists without changes**:
  ```python
  merged_list = x.merge_no_changes(y)
  ```

### Finding Elements

- **Find the first occurrence of a value**:
  ```python
  pos = x.search(10)
  ```

## Example

```python
x = doublly_positional_not_sentinel_list()
x.add_first(6)
x.add_first(4)
x.add_first(2)
x.add_last(555)

print(x)  # Output: (2)  (4)  (6)  (555)

# Reverse the list
reversed_list = x.reverse()
print(reversed_list)  # Output: (555)  (6)  (4)  (2)

# Sort the list in ascending order
sorted_list = x.ordering_asending()
for node in sorted_list:
    print(node.data)  # Output: 2, 4, 6, 555
```

## Notes

- The list does **not use sentinel nodes**, which simplifies the implementation but requires careful handling of boundary conditions.
- The `_position` class acts as a handle to nodes, allowing for safe and efficient manipulation of the list.
- The list supports **1-based indexing** for positional operations.

