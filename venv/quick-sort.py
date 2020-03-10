# program to implement quick sort
# Adam Maser
# CSC 330 - Language Design and Implementation
# 3.9.2020


def partition(arr, low, high):
    i = low - 1  # get index of low
    pivot = arr[high]  # get pivot
    # do the sorting
    for j in range(low, high):
        if arr[j] <= pivot:
            # increment index
            i += 1
            # swap elements
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        # get index that splits array into partitions
        index = partition(arr, low, high)
        # sort elements before and after partition recursively
        quicksort(arr, low, index - 1)
        quicksort(arr, index + 1, high)


def main():
    # test array
    arr = [23, 6, 16, 2, 5, 11, 8, 3, 44, 3]
    length = len(arr)
    # call quicksort method
    quicksort(arr, 0, length - 1)
    # print array
    print("Sorted Array:")
    print("-------------")
    for i in range(length):
        print("Index", str(i) + ":", arr[i])


# call main function
main()
