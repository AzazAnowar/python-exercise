"""
Write a program that takes a list of integers and sorts it without using built-in
functions. Implement your own sorting algorithm, such as bubble sort or selection sort.
"""

# ASCENDING ORDER SELECTION SORT
def asc_selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# DESCENDING ORDER SELECTION SORT
def dsc_selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


unsorted_list1 = [12, 25, 11, 34, 90, 22]
unsorted_list2 = [5,4,3,2,1,0]
unsorted_list3 = [0,1,2,3,4,5]
#print(len(unsorted_list1))

sorted_list1 = asc_selection_sort(unsorted_list1)
print("Sorted Elements : ", sorted_list1)


sorted_list2 = asc_selection_sort(unsorted_list2)
print("Sorted Elements : ", sorted_list2)

sorted_list3 = dsc_selection_sort(unsorted_list2)
print("Sorted Elements : ", sorted_list3)
