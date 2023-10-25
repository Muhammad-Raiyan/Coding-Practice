def find_pairs(arr1, arr2, target):
    diff_map = {}
    ans = []
    for i, val in enumerate(arr1):
        diff = target - val
        diff_map[diff] = i

    for i, val in enumerate(arr2):
        if val in diff_map:
            ans.append((arr1[diff_map[val]], arr2[i]))

    # print(ans)
    return list(set(ans))


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)


"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
