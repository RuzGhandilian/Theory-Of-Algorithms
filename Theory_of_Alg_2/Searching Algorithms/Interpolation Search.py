def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50

result = interpolation_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
