def item_in_common(list1: list, list2: list) -> None | int:
    unique_items = set()
    for item in list1:
        unique_items.add(item)

    for item in list2:
        if item in unique_items:
            return True
        unique_items.add(item)

    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))


"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
