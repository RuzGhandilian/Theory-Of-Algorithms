def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


x = [2, 5, 1, 4, 5, 2, 4, 6, 8, 7, 5, 6, 9, 7, 3, 6, 7, 8, 4]
bubble_sort(x)
print(x)
