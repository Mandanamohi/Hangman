import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = self._choose_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _choose_word(self):
        return random.choice(self.word_list)

    def _update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def _handle_correct_guess(self, guess):
        print(f"Good guess! '{guess}' is in the word.")
        self._update_word_guessed(guess)

    def _handle_incorrect_guess(self, guess):
        print(f"Sorry, '{guess}' is not in the word.")
        print(f"You have {self.num_lives} lives left.")
        self.num_lives -= 1

    def _is_game_over(self):
        if self.num_lives == 0:
            print("You lost!")
            return True
        elif self.num_letters == 0:
            print("Congratulations. You won the game!")
            return True
        return False

    def check_guess(self, guess):
        if guess in self.word:
            self._handle_correct_guess(guess)
            return True
        else:
            self._handle_incorrect_guess(guess)
            return False
 
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                print("You lost!")
              

    def ask_for_input(self):
        while True:
            print("Word to guess:", self.word_guessed)  # Print the word to be guessed
            print("Letters already guessed:", self.list_of_guesses)
            guess = input("Guess a letter: ").lower()  # Convert input to lowercase
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            
            guess = input("Enter your guess (a single letter): ")
            if not self._is_valid_guess(guess):
                continue

            if self._is_guess_already_tried(guess):
                print("You already tried that letter!")
                continue

            if self.check_guess(guess):
                self.list_of_guesses.append(guess)
                break

    def _is_valid_guess(self, guess):
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False
        return True

    def _is_guess_already_tried(self, guess):
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            return True
        return False

    def play_game(self):
        while not self._is_game_over():
            self.ask_for_input()

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


word_list = ['apple', 'banana', 'orange']
play_game(word_list)

