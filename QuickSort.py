def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


x = [2, 5, 1, 7, 2, 4, 6, 7, 2, 4, 2, 4, 2, 4, 6, 8, 9, 9]
y = quick_sort(x)
print(y)
