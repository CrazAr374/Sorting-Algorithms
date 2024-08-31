import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def print_complexities(algo):
    complexities = {
        "Bubble Sort": {"Time": "O(n^2)", "Space": "O(1)"},
        "Insertion Sort": {"Time": "O(n^2)", "Space": "O(1)"},
        "Selection Sort": {"Time": "O(n^2)", "Space": "O(1)"},
        "Merge Sort": {"Time": "O(n log n)", "Space": "O(n)"},
        "Quick Sort": {"Time": "O(n^2)", "Space": "O(log n)"}
    }
    print(f"\n{algo} - Time Complexity: {complexities[algo]['Time']}, Space Complexity: {complexities[algo]['Space']}")

def main():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("\nChoose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    
    choice = int(input("Enter your choice (1-5): "))

    sorted_arr = []
    start_time = time.time()
    
    if choice == 1:
        sorted_arr = bubble_sort(arr.copy())
        print_complexities("Bubble Sort")
    elif choice == 2:
        sorted_arr = insertion_sort(arr.copy())
        print_complexities("Insertion Sort")
    elif choice == 3:
        sorted_arr = selection_sort(arr.copy())
        print_complexities("Selection Sort")
    elif choice == 4:
        sorted_arr = merge_sort(arr.copy())
        print_complexities("Merge Sort")
    elif choice == 5:
        sorted_arr = quick_sort(arr.copy())
        print_complexities("Quick Sort")
    else:
        print("Invalid choice!")

    end_time = time.time()

    if sorted_arr:
        print(f"Sorted Array: {sorted_arr}")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
