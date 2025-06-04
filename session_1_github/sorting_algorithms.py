import time
import random


def merge_sort_v1(arr):

	"""Implement merge sort algorithm"""
	if len(arr) <= 1:
		return arr
	
	mid = len(arr) // 2

	left = merge_sort_v1(arr[:mid])
	right = merge_sort_v1(arr[mid:])

	
	return merge(left, right)

def merge(left, right):
	"""Helper function to merge two sorted arrays"""
	result = []
	i = j = 0
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	
	result.extend(left[i:])
	result.extend(right[j:])
	return result

def insertion_sort(arr):
	"""Implement insertion sort algorithm"""
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		
		arr[j + 1] = key
	return arr

def quick_sort(arr):
	"""Implement quick sort algorithm"""
	if len(arr) <= 1:
		return arr
	
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	
	return quick_sort(left) + middle + quick_sort(right)

# Demonstration with sample data
if __name__ == "__main__":
	sample_data = [64, 34, 25, 12, 22, 11, 90]
	
	print("Original array:", sample_data)
	print()
	
	# Merge Sort

	merge_sort_v1ed = merge_sort_v1(sample_data.copy())
	print("Merge Sort:", merge_sort_v1ed)

	
	# Insertion Sort
	insertion_sorted = insertion_sort(sample_data.copy())
	print("Insertion Sort:", insertion_sorted)
	
	# Quick Sort
	quick_sorted = quick_sort(sample_data.copy())
	print("Quick Sort:", quick_sorted)
	
	# Performance comparison with larger dataset
	
	large_data = [random.randint(1, 1000) for _ in range(1000)]
	
	print("\nPerformance comparison on 1000 elements:")
	
	# Merge Sort timing
	start = time.time()

	merge_sort_v1(large_data.copy())

	print(f"Merge Sort: {time.time() - start:.4f} seconds")
	
	# Insertion Sort timing
	start = time.time()
	insertion_sort(large_data.copy())
	print(f"Insertion Sort: {time.time() - start:.4f} seconds")
	
	# Quick Sort timing
	start = time.time()
	quick_sort(large_data.copy())
	print(f"Quick Sort: {time.time() - start:.4f} seconds")