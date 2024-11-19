# Задача "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words = []
    if other_words.count(root_word) == 1:
        same_words.append(other_words)
        print(same_words)
        print(root_word, other_words)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
