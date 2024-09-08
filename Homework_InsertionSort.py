def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


x = [54, 41, 63, 74, 21, 95, 74, 86, 32, 10]
insertion_sort(x)
print("Sorted array:", x)
