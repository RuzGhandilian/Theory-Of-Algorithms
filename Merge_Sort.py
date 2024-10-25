def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left, right = merge_sort(L[:mid]), merge_sort(L[mid:])
    return merge(left, right)


def merge(left, right):
    res, l, r = [], 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    return res + left[l:] + right[r:]


# Example usage
x = [64, 25, 32, 12, 66, 78, 1, 6, 3, 2, 7, 8, 12, 22, 11]
print(merge_sort(x))
