def binary_search(arr, x):
    high = len(arr)
    low = -1
    counter = 0
    while high >= low:
        counter += 1
        mid = int((low + high) / 2)
        if arr[mid] == x:
            return mid, counter
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
        if low == high:
            return "Not found"
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(a, 1))
