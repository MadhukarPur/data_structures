'''
    Linear Search - The linear search algorithm is used to find an element within a list. In this algorithm, 
                we sequentially check each element of the list until the desired element is found.

    Applications of Linear Search
        Linear search is not an efficient algorithm. That being said, we can use linear search in the 
        following situations:
            When the list is small. For example, 10, 50 or 100 elements.
            When searching through an unsorted list. Unlike some other algorithms, linear search does not 
            require the list to be sorted.
    
    Time Complexity:
        Best Case:  O(1)
        Worst Case: O(n)
        Average Case: O(n)
'''
def linear_serach(lst,target):
    for idx,value in enumerate(lst):
        if value == target:
            return idx
    return None


'''
    Binary Search - binary search can only be implemented in a sorted list. If the elements in the list 
            are unsorted, we need to sort the elements first.

    Applications of Binary Search
        Binary search is used in scenarios where the data is already sorted (or can be sorted easily). 
        This includes:
            Database search: Binary search can be used to quickly search through large databases to find 
                        specific records or elements.
            Search Engines: Binary search can be used to locate a word or phrase in a sorted list of indexed terms.

    Time Complexity:
        Best Case: O(1)
        Worst Case : O(log n)
        Average Case: O(log n)
'''
def binary_search(lst, target,low,high):
    if low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        
        elif target < lst[mid]:
            return binary_search(lst,target,low,mid - 1)
        else:
            return binary_search(lst,target,mid+1,high)
    else:
        return None

lst = [4, 5, 9, 12, 55, 79, 88, 99]
target = 12
output = binary_search(lst,target,0,len(lst)-1)
if output:
    print(f'Target value {target} found at {output}')
else:
    print(f'Target value {target} not found!')
