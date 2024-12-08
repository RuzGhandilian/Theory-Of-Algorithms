def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [15, 22, 33, 47, 58, 64, 72, 85, 99]
target = 47

result = linear_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
