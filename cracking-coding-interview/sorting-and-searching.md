# Common sorting algorithms

- Bubble sort

Runtime: O(N^2)
Memory: O(1)  -> in-place
Idea: "bubble" the maximum in each i-th iteration to the end of the arrray

- Selection sort
Runtime: O(N^2)
Memory: O(1) -> in-place
Idea: Pick the minimum in each iteration and place it in it's corresponding position

Property: Runs a number of linear exchanges (not comparissons). Why? Because
it only exchanges when it finds the minimum. Then per each element, I only exchange 1 time (but per each element, I do N - i comparissons, where i is my position)


- Insertion sort (doesn't appear in cracking the coding interview, but nice to know)
*Invariant* Always the sub-array in the left is sorted. 
Idea: To add the i-th value in it's corresponding position on a already sorted sub-array (the array on the left)


*Note:* Timsort is used in Python and is a hybrid, stable sorting algorithm that used both
merge sort and insertion sort :)

Runtime: O(N^2)
Memory: O(1)

