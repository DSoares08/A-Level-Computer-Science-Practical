def insertion_sort(arr):
    for i in range (1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = anchor
arr = [8, 8, 6, 5, 4, 3, 2, 1]
insertion_sort(arr)
print(arr)
