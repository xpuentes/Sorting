# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 10, 15, 11]
print(bubble_sort(arr2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr