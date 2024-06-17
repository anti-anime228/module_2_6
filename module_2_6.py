def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for o_word in other_words:
        o_word = o_word.lower()
        if root_word in o_word or o_word in root_word:
            same_words.append(o_word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
