def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    low = i // 2
    high = min(i, len(arr) - 1)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50

result = exponential_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
