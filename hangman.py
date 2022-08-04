import random
def get_random_word(dictfile="/usr/share/dict/words"):
    good_words = []
    with open(dictfile) as words:
        for i in words:
            i = i.strip()
            if len(i) < 6:
                continue
            if not i.isalpha():
                continue
            if i[0].isupper():
                continue
            good_words.append(i)

    return random.choice(good_words)


def mask_word(word, guesses):
    return "------"
