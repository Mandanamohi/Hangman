import random
class Hangman:
     def __init__(self, word_list, num_lives=5):
       
        # Step 3: Initialize attributes
        self.word_list = word_list
        self.word = self._choose_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        def _choose_word(self):
            return random.choice(self.word_list)

# Example usage:
word_list_example = ['apple', 'banana', 'orange', 'grape', 'kiwi']
hangman_game = Hangman(word_list_example)

# Accessing attributes:
print(f"Word to guess: {hangman_game.word}")
print(f"Word guessed so far: {hangman_game.word_guessed}")
print(f"Number of lives: {hangman_game.num_lives}")
print(f"List of guesses: {hangman_game.list_of_guesses}")