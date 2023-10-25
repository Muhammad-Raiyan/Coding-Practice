def has_unique_chars(my_str):
    my_set = set()

    for ch in my_str:
        if ch in my_set:
            return False
        my_set.add(ch)

    return True


print(has_unique_chars("abcdefg"))  # should return True
print(has_unique_chars("hello"))  # should return False
print(has_unique_chars(""))  # should return True
print(has_unique_chars("0123456789"))  # should return True
print(has_unique_chars("abacadaeaf"))  # should return False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""
