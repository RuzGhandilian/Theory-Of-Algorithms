def selection_sort(L):
    for i in range(len(L)):
        min_idx = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_idx]:
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]
    return L


# Example usage
x = [64, 25, 32, 12, 66, 78, 1, 6, 3, 2, 7, 8, 12, 22, 11]
print(selection_sort(x))
