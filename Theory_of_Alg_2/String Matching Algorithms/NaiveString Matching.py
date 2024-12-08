def find_pattern(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            print("Pattern found at index", i)
            return i

    print("Pattern not found")
    return -1


text = "asdnjnfajefnjnijuhhuew"
pattern = "jnfaje"
find_pattern(text, pattern)
