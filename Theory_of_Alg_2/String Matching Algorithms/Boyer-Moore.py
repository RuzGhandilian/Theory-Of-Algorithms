def create_bad_char_table(pattern):
    bad_char_table = {}
    for i in range(len(pattern)):
        bad_char_table[pattern[i]] = i
    return bad_char_table


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char_table = create_bad_char_table(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {i}")
            i += m
        else:
            bad_char_shift = bad_char_table.get(text[i + j], -1)
            i += max(1, j - bad_char_shift)


text = "huhfhjsbfsehfiejuuihuhuhhbhbuhuuhevhbudeaahdae"
pattern = "jsbfsehf"
boyer_moore_search(text, pattern)
