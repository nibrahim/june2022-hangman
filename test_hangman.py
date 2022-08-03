import hangman

def test_get_random_word_min_length_6():
    word = hangman.get_random_word()
    assert len(word) >= 6

def test_get_random_word_no_non_alphanum():
    word = hangman.get_random_word()
    assert word.isalpha()

def test_get_random_word_no_proper_noun():
    word = hangman.get_random_word()
    assert not word[0].isupper()

def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'hospitalized', 'car', 'Abraham', "mercury's"]:
            f.write(i+"\n")

    word = hangman.get_random_word(my_dict)
    for _ in range(5):
        assert word in ["hospitalized", 'ambulances']

# RED - Implement a test that will fail
# GREEN - Make the test pass
# REFACTOR - Adjust the code so that all tests pass and code is improved
