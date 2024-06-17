# root_word = input("Введите число-ключ: ").lower()
# other_words_input = input("Введите остальные слова через запятую ',': ").lower()
# other_words = other_words_input.split(",")  # Разбиваем строку по ,

#рабочая
# def single_root_words(root_word, *other_words):
#     same_words = []
#     for o_word in other_words:
#         if root_word in o_word:
#             same_words.append(o_word)
#     return same_words
# print(single_root_words(root_word, other_words))


# def single_root_words(root_word, *other_words):
#     same_words = []
#     for o_word in other_words:
#         if root_word in o_word:
#             same_words.append(o_word)
#     return same_words

phrase = ('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
word = 'rich'
def single_root_words():
    same_words = []
    for i in phrase:
        if word in phrase:
            same_words.append(phrase)
    print(same_words)
single_root_words()
