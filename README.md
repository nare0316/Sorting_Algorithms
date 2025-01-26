1️⃣2️⃣3️⃣ Sorting Algorithms This repository contains implementations of several classic sorting algorithms in Python. Each algorithm is designed to demonstrate the fundamental principles of sorting and provides a clear understanding of how different sorting strategies perform under different conditions.

📎 Sorting Algorithms Implemented:

Bubble Sort: Bubble Sort is a simple sorting algorithm where each pair of adjacent elements is compared and swapped if they are in the wrong order. The algorithm repeatedly makes passes through the list until no swaps are required, indicating that the list is sorted. Time Complexity: O(n²) Space Complexity: O(1)
Selection Sort: Selection Sort works by repeatedly finding the minimum element from the unsorted portion of the list and swapping it with the element at the beginning of the unsorted portion. Time Complexity: O(n²) Space Complexity: O(1)
Insertion Sort: Insertion Sort builds the sorted array one item at a time by repeatedly picking the next element from the unsorted part and inserting it into the correct position in the sorted part. Time Complexity: O(n²) Space Complexity: O(1)
Merge Sort: Merge Sort is a divide and conquer algorithm. It divides the array into two halves, recursively sorts both halves, and then merges them together in sorted order. Time Complexity: O(n log n) Space Complexity: O(n)
Quick Sort:
▶️ QuickSort1 (Pivot = Last Element): This implementation selects the last element as the pivot and partitions the array around this pivot such that elements smaller than the pivot are on the left and elements larger are on the right.

▶️ QuickSort2 (Pivot = First Element): This implementation selects the first element as the pivot and partitions the array around this pivot.

▶️ QuickSort3 (Pivot = Random Element): This implementation randomly selects a pivot and partitions the array based on this pivot, helping to mitigate worst-case performance. Time Complexity: O(n log n) on average, O(n²) in the worst case Space Complexity: O(log n) (due to recursion stack)

Counting Sort: Counting Sort is a non-comparative sorting algorithm that works by counting the number of occurrences of each distinct element in the array. It uses this count information to place each element directly in its correct position in the sorted array. Time Complexity: O(n + k), where n is the number of elements and k is the range of the input. Space Complexity: O(k) for the auxiliary count array.
Radix Sort: Radix Sort is a non-comparative sorting algorithm that sorts numbers digit by digit, starting from the least significant digit to the most significant digit. It uses a stable auxiliary sort (counting sort) on each digit. Time Complexity: O(nk) where n is the number of elements and k is the number of digits in the largest number Space Complexity: O(n)
📎 Features:

Multiple Sorting Techniques: This repository showcases a variety of sorting algorithms, ranging from simple algorithms like Bubble Sort to more efficient ones like Merge Sort and Quick Sort.
Educational Purpose: Each algorithm is implemented with a clear structure to help understand the underlying mechanics of sorting. 3 Contributions: Feel free to fork, modify, and contribute to the repository. Improvements, bug fixes, and additional sorting algorithms are always welcome!