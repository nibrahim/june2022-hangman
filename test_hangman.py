import hangman

def test_get_random_word_min_length_6():
    word = hangman.get_random_word()
    assert len(word) >= 6
