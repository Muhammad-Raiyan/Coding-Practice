def longest_consecutive_sequence(seq):
    if len(seq) == 0:
        return 0
    if len(seq) == 1:
        return 1
    seq.sort()
    max_len = 1
    temp = 1
    for i, val in enumerate(seq):
        if i == 0:
            temp = 1
        elif val == seq[i - 1]:
            continue
        elif val - seq[i - 1] == 1:
            temp += 1
            max_len = max(max_len, temp)
        else:
            temp = 1
        print(val, seq[i - 1], temp, max_len)

    return max_len


# print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
print(longest_consecutive_sequence([1, 2, 2, 3, 4, 5]))
# print(longest_consecutive_sequence([5, 5, 5, 5]))

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
