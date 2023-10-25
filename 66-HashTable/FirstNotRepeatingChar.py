def first_non_repeating_char(str):
    dict = {}
    for ch in str:
        dict[ch] = dict.get(ch, 0) + 1

    for ch in str:
        if dict[ch] == 1:
            return ch


print(first_non_repeating_char("leetcode"))

print(first_non_repeating_char("hello"))

print(first_non_repeating_char("aabbcc"))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
