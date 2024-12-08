def IsPalindrome(txt):
    for i in (range(int(len(txt) / 2))):
        if txt[i] != txt[0 - (i + 1)]:
            return False
    return True


def LongestPalindrome(txt):
    longest = ""
    n = len(txt)

    for i in range(n):
        for j in range(i, n):
            sub = txt[i:j + 1]
            if IsPalindrome(sub) and len(sub) > len(longest):
                longest = sub
    return longest


def IsPalindromable(txt):
    # Count the frequency of each character
    freq = {}
    for char in txt:
        freq[char] = freq.get(char, 0) + 1

    oddcount = 0
    for count in freq.values():
        if count % 2 != 0:
            oddcount += 1

    return oddcount <= 1


print(IsPalindrome('abdsaadba'))
print(IsPalindromable('asbsaab'))
print(LongestPalindrome('sgsrggegegegegegegabdaadbagsrghsrhsreweae'))
print(IsPalindromable('asbsabsb'))
