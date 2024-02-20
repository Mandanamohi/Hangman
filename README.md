 1)check that the input is a single character:

user_input = input("Enter a character: ")

if len(user_input) == 1 and user_input.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    
This code checks if the length of the input is equal to 1 (len(user_input) == 1) and if the input consists of alphabetical characters only (user_input.isalpha()). If both conditions are true, it prints "Good guess!". Otherwise, it prints "Oops! That is not a valid input.





2) Write code that will continuously ask the user for a letter and validate it.

while True:
    guess = input("Guess a letter: ")
    
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guessed:", guess)

This script will continuously ask the user to guess a letter. It validates the guess to ensure it is a single alphabetical character. If the guess passes the checks, it breaks out of the loop and prints the guessed letter. If the guess does not pass the checks, it prints a message prompting the user to enter a valid letter.

3)Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.
For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".
import random

 List of secret words:
words = ["apple", "banana", "orange", "grape", "pear"]


secret_word = random.choice(words)

while True:
    guess = input("Guess a letter: ")
    
    if len(guess) == 1 and guess.isalpha():
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guessed:", guess)
print("The secret word was:", secret_word)

This code now checks if the guessed letter (guess) is in the secret_word. If the guess is correct, it prints a message indicating that the guess is in the word. If the guess is incorrect, it prints a message indicating that the guess is not in the word.**





4) Create function to run the checks.
   import random


words = ["apple", "banana", "orange", "grape", "pear"]


secret_word = random.choice(words)

def check_guess(guess):
    guess = guess.lower()  # Step 2: Convert the guess into lower case.
    if guess in secret_word:  # Step 3: Move the code to check if the guess is in the word.
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)  # Step 3: Call the check_guess function to check if the guess is in the word.


ask_for_input()

This code now separates the functionality into two functions: check_guess and ask_for_input. The check_guess function checks if the guessed letter is in the word, and the ask_for_input function handles the input validation and calls check_guess to check the guessed letter against the secret word. Finally, we call ask_for_input outside the function definitions to test the code.




5)

 import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))


hangman_game = Hangman(['apple', 'banana', 'orange'])
print("Word to guess:", hangman_game.word)
print("Word guessed so far:", hangman_game.word_guessed)
print("Number of lives:", hangman_game.num_lives)
print("Word list:", hangman_game.word_list)
print("List of guesses:", hangman_game.list_of_guesses)
print("Number of unique letters in the word:", hangman_game.num_letters)

In this code, the Hangman class is defined with an __init__ method that initializes the attributes as described. The word attribute is randomly chosen from the provided word_list, and word_guessed is initialized with underscores representing the letters yet to be guessed. num_letters is calculated as the number of unique letters in the word. Finally, num_lives is initialized either with the provided value or the default value of 5, and list_of_guesses is initialized as an empty list. We also test the class by creating an instance of Hangman and printing its attributes.





6) Create  methods for running the checks:
   
   import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guessed letter to lower case
        if guess in self.word:  # Check if the guess is in the word
            print(f"Good guess! '{guess}' is in the word.")
        # You will continue with the logic of the check_guess method in the next task.

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  # Call the check_guess method
                self.list_of_guesses.append(guess)  # Append the guess to the list_of_guesses


hangman_game = Hangman(['apple', 'banana', 'orange'])
hangman_game.ask_for_input()

In this code, the check_guess method checks if the guessed letter is in the word and prints a message accordingly. The ask_for_input method prompts the user to guess a letter and handles invalid input or repeated guesses. It calls the check_guess method if the input is valid and not already guessed, and appends the guess to the list_of_guesses. Finally, we test the code by calling the ask_for_input method.


 
 
 
 7) modified check_guess method:
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:  
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  
            self.num_letters -= 1  

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)  


hangman_game = Hangman(['apple', 'banana', 'orange'])
hangman_game.ask_for_input()
print("Word guessed so far:", hangman_game.word_guessed)
print("Number of unique letters in the word:", hangman_game.num_letters)

In this modification, after confirming that the guessed letter is in the word, the method iterates through each letter in the word. For each letter that matches the guess, it replaces the corresponding underscore in word_guessed with the guess. Then, it decreases the num_letters variable by 1 to reflect that one more letter has been correctly guessed.




8)Define what happens if the guess is not in the word you are trying to guess.
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower() 
        if guess in self.word:  
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  
            self.num_letters -= 1  # Reduce the variable num_letters by 1
        else:  
            self.num_lives -= 1  # Reduce num_lives by 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)  


hangman_game = Hangman(['apple', 'banana', 'orange'])
hangman_game.ask_for_input()
print("Word guessed so far:", hangman_game.word_guessed)
print("Number of unique letters in the word:", hangman_game.num_letters)

In this modification, when the guessed letter is not in the word, the check_guess method decreases the num_lives by 1 and prints a message indicating that the guess is incorrect and informing the player about the remaining number of lives.



9)Create a function that will run all the code to run the game as expected.

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:  
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess 
            self.num_letters -= 1  
        else:  
            self.num_lives -= 1  
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)  
            if self.num_lives == 0 or self.num_letters == 0:
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


word_list = ['apple', 'banana', 'orange']
play_game(word_list)

In this code, the play_game function orchestrates the game flow. It initializes the number of lives, creates an instance of the Hangman class with the provided word list and number of lives, and then enters a while loop to play the game. It checks if the number of lives is zero, in which case the game ends and the player loses. If not, it checks if there are still letters left to guess, and if so, it calls the ask_for_input method to prompt the player for a guess. Finally, it checks if the player has won by guessing all the letters in the word. Outside the function, we call play_game with the word list to start the game.


