def group_anagrams(word_list):
    if len(word_list) == 0:
        return word_list
    anagrams_dict = {}

    temp = word_list[0]
    anagrams_dict[temp] = []

    for item in word_list:
        unique_keys = list(anagrams_dict.keys())
        for key in unique_keys:
            if are_anagram(key, item):
                anagrams_dict[key].append(item)
            else:
                anagrams_dict[item] = [item]

            # print(anagrams_dict)

    return list(anagrams_dict.values())


def are_anagram(left, right):
    my_set = set()

    for ch in left:
        my_set.add(ch)

    for ch in right:
        if ch not in my_set:
            return False
    return True


def group_anagrams2(word_list):
    anagrams_dict = {}

    for word in word_list:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]

    return list(anagrams_dict.values())


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
