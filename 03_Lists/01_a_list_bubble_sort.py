"""
Write a program that takes a list of integers and sorts it without using built-in
functions. Implement your own sorting algorithm, such as bubble sort or selection sort.
"""

"""
# TOO MANY ITERATION IN THIS LOOP. WE CAN SEE THAT THE LAST POSITION WILL ALWAYS LARGEST IS ASCENDING ORDER
# SO WE CAN DO N-1 FOR 2nd PASS
def bubble_sort(arr):
    n = len(arr)

    for passes in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
"""

# ASCENDING ORDER BUBBLE SORT
def asc_bubble_sort(arr):
    n = len(arr)

    for passes in range(n):
        for j in range(0, n-1-passes):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# DESCENDING ORDER BUBBLE SORT
def dsc_bubble_sort(arr):
    n = len(arr)

    for passes in range(n):
        for j in range(0, n-1-passes):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

unsorted_list1 = [12, 25, 11, 34, 90, 22]
unsorted_list2 = [5,4,3,2,1,0]
unsorted_list3 = [0,1,2,3,4,5]
#print(len(unsorted_list1))

sorted_list1 = asc_bubble_sort(unsorted_list1)
print("Sorted Elements : ", sorted_list1)

sorted_list2 = asc_bubble_sort(unsorted_list2)
print("Sorted Elements : ", sorted_list2)

sorted_list3 = dsc_bubble_sort(unsorted_list2)
print("Sorted Elements : ", sorted_list3)
