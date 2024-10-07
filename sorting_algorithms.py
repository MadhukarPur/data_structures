'''
   Bubble Sort - Bubble sort works by comparing two adjacent elements and swapping them if needed.
   Application of Bubble_sort:
        When to use bubble sort?
            Use bubble sort for Small datasets.
            When simplicity is more important than efficiency.
            When the data is already partially sorted.
        
        When not to use bubble sort?
            Avoid bubble sort for large datasets and performance-critical applications. 
            In such cases, sorting algorithms like merge sort or quick sort are more suitable.

    Time Complexity: O{n^2}
    Space Complexity: O(1)
'''
def bubble_sort(lst):
    # outer loop to access each list element
    swapped = False
    for i in range(len(lst)-1):
        # inner loop to compare list elements
        for j in range(len(lst)-1-i):
            # swap elements if necessary
            # if lst[j] > lst[j+1]: #Ascending order
            if lst[j] < lst[j+1]: #Descending order
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swapped: # if no swapping means the list is already sorted. Exit from the loop.
            break
    return lst

''' 
    Selection Sort - Selection sort works by repeatedly selecting the smallest (or largest) unsorted element and placing it towards the beginning of the list.
    Applications of Selection Sort
        When to use selection sort?
            Use selection sort for small lists where simplicity is more important than speed.
            While this also applies to bubble sort, selection sort generally requires fewer swaps.
            Therefore, it's favored over bubble sort when the cost of swapping significantly outweighs the cost of comparisons.

        When not to use selection sort?
            Avoid selection sort for larger lists or situations where speed is crucial. Merge sort and quick sort are preferable for larger lists.
    
    Time Complexity: O{n^2}
    Space Complexity: O(1)
'''
def selection_sort(lst):
    for i in range(len(lst)):
        # assume the first unsorted element is the minimum
        min_index = i
        # iterate over unsorted elements
        for j in range(i+1,len(lst)):
            # find index of the smallest element in the unsorted part of the list
            if lst[j] < lst[min_index]:
                min_index = j
        
        # swap the smallest element with the first element of the unsorted part 
        lst[min_index],lst[i] = lst[i],lst[min_index]

    return lst

''' 
    Insertion Sort - Insertion sort works by repeatedly taking an element from the unsorted portion of the list and 
                inserting it into its correct position within the already-sorted portion
    
    Applications of Insertion Sort:
        When to use insertion sort?
            Use insertion sort for small lists or when your data is mostly in order. It's simple and works well when dealing with a limited number of items.

        When not to use insertion sort?
            Avoid insertion sort for larger lists or when speed is essential. It can become slow for bigger datasets.
            In those cases, opt for faster algorithms like merge sort or quick sort for better performance.
    
    Time Complexity: O{n^2}
    Space Complexity: O(1)
'''
def insertion_sort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1

        while j>=0 and key < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        
        lst[j+1] = key
    return lst

''' 
    Merge Sort - Merge sort breaks a list into multiple sublists, and each sublist is then sorted individually. Then, the sorted sublists are combined 
    to form the sorted list. This strategy is known as divide-and-conquer.
    
    Applications of Merge Sort
        Use merge sort to sort large amounts of data accurately and efficiently.
    
    Time Complexity = O(n log n)
    Space Complexity = O(n)
'''
def merge_sort(lst):
    # base condition: recursion ends if the length of the list is 1 or less 
    if len(lst)<=1:
        return lst
    
    mid = len(lst)//2
    # get the left half of the list and further divide it using recursion
    left_partition = merge_sort(lst[:mid])
    
    # get the right half of the list and further divide it using recursion
    right_partition = merge_sort(lst[mid:])
    
    # call the merge() function  combine list recursively
    return merge(left_partition,right_partition)

def merge(left, right):
    output = [ ]
    i,j = 0,0
    while i < len(left) and j < len(right): 
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j]) 
            j += 1
 
    # copy the remaining elements to output
    output.extend(left[i:])
    output.extend(right[j:])
    return output

'''
 Quick Sort - The quick sort algorithm selects a random element of the list as the pivot and partitions the remaining elements into two sublists: 
            those less than the pivot and those greater than the pivot. The sublists are then sorted recursively.

 Applications of Quick Sort
    Use quick sort for quickly sorting large datasets. It's efficient and works best when dealing with diverse data.

    When not to use quick sort?
        Avoid quick sort if you need a sorting algorithm that maintains the order of equal elements. Also, quick sort can be slow in worst-case scenarios.  
    
    Time Complexity : O(n log n)
    Space Complexity: O(log n)
'''
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()

    left, right = [], []
    for element in lst:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

'''
    Counting Sort - Counting sort is a way to arrange the items in a list by counting how many times each item appears. We then put the elements in order 
                    based on those counts.
    Applications of Counting Sort
        When to use counting sort?
            Counting sort is highly efficient for sorting non-negative integers within a limited range.
        When not to use counting sort?
            Avoid using counting sort when dealing with a wide range of values or when you have negative integers.

    Time complexity : O(n + max)
    space Complexity : O(max)
'''
def counting_sort(lst):
    if len(lst) <= 1:
        return lst

    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    for num in lst:
        counting_list[num]+=1

    sorted_list = []
    for index,value in enumerate(counting_list):
        sorted_list.extend([index]*value)

    return sorted_list

lst = [15,16,6,8,5,32,10]
print(lst)
print(counting_sort(lst))
