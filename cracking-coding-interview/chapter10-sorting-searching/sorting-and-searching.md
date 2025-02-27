# Common sorting algorithms

- Bubble sort

Runtime: O(N^2)
Memory: O(1)  -> in-place
*Invariant:* TO CHECK Always the sub-array in the right is sorted
Idea: "bubble" the maximum in each i-th iteration to the end of the arrray


- Selection sort
Runtime: O(N^2)
Memory: O(1) -> in-place
*Invariant* Always the sub-array in the left is sorted. 
Idea: Pick the minimum in each iteration and place it in it's corresponding position

Property: Runs a number of linear exchanges (not comparissons). Why? Because
it only exchanges when it finds the minimum. Then per each element, I only exchange 1 time (but per each element, I do N - i comparissons, where i is my position)


- Insertion sort (doesn't appear in cracking the coding interview, but nice to know)
Runtime: O(N^2)
Memory: O(1)


*Invariant* Always the sub-array in the left is sorted. 
Idea: To add the i-th value in it's corresponding position on a already sorted sub-array (the array on the left)


*Note:* Timsort is used in Python and is a hybrid, stable sorting algorithm that used both
merge sort and insertion sort :)

Difference with selection sort:
- Elements in the oredered sub-array (the array in the left) can still be changed (not in their final position)
- Running time depends on the initial order of the items in the input, while selection sort always runs in the same time
	- *Example:* If array already in ordered or almost in ordered, then insertion sort is way much faster than selection sort 
	
*To remember* Insertion sort works better for partially-sorted arrays than big old quicksort and mergesort


- Merge sort

*Idea*: Halve the array, sort each half and then merge the sorted sub-arrays in linear time. Because they are sorted, you can just iterate over them w/two indexes and start adding to the final array the elements.

Runtime: O(N log N)
Space: O(N) -> we need a copy of the array to make mergesort to work

