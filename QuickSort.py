def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [a for a in arr[1:] if a <= pivot]
        right = [a for a in arr[1:] if a > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


x = [64, 25, 32, 12, 66, 78, 1, 6, 3, 2, 7, 8, 12, 22, 11]
print(quick_sort(x))
