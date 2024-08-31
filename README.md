# Sorting Algorithms

This repository contains implementations of various sorting algorithms in Python. Each algorithm has been implemented with explanations of their time and space complexities.

## Algorithms Included

1. **Bubble Sort**
   - **Time Complexity**: O(n^2)
   - **Space Complexity**: O(1)
   - **Description**: Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

2. **Insertion Sort**
   - **Time Complexity**: O(n^2)
   - **Space Complexity**: O(1)
   - **Description**: Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

3. **Selection Sort**
   - **Time Complexity**: O(n^2)
   - **Space Complexity**: O(1)
   - **Description**: Selection Sort is an in-place comparison sorting algorithm. It has an O(n^2) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort.

4. **Merge Sort**
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(n)
   - **Description**: Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the order of equal elements is the same in the input and output.

5. **Quick Sort**
   - **Time Complexity**: O(n^2) in the worst case, O(n log n) on average
   - **Space Complexity**: O(log n)
   - **Description**: Quick Sort is an efficient sorting algorithm. Developed by Tony Hoare in 1959, it is still a commonly used algorithm for sorting.

## How to Run the Code

To run the code, clone the repository and execute the Python files with the sorting algorithms you wish to test.

```bash
git clone https://github.com/your-username/Sorting-Algorithms.git
cd Sorting-Algorithms
python sorting_script.py
```
### 5. **Add Python Code for Each Algorithm**:

Create separate Python files for each sorting algorithm, such as `bubble_sort.py`, `insertion_sort.py`, etc., and add the corresponding Python code to each file. 

### Example Python Code for `bubble_sort.py`:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array is:", bubble_sort(arr))
```
```
git add .
git commit -m "Added sorting algorithms and README"
git push origin main
