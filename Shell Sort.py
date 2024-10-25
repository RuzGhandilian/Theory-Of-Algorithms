def shell_sort(L):
    n = len(L)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = L[i]
            j = i
            while j >= gap and L[j - gap] > temp:
                L[j] = L[j - gap]
                j -= gap
            L[j] = temp
        gap //= 2

    return L


# Example usage
x = [64, 25, 32, 12, 66, 78, 1, 6, 3, 2, 7, 8, 12, 22, 11]
print(shell_sort(x))
