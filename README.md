A Hangman game similar to `/usr/games/hangman` written as a TDD exercise


# Hangman API
## `hangman.py`
    Functions
    1. `get_random_word` 
       - Inputs - No inputs
       - Output - Returns a random word from `/usr/share/dict/words` satisfying the following conditions
         1. Should be atleast 6 letters long
         2. Should not have any non alphabetical characters
         3. No proper nouns (no words with capital initial letter)
       
        w = hangman.get_random_word()
        print(w) # might be 'elephant'
