import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialization code...

    def _choose_word(self):
        # Helper method...

    def check_guess(self, guess):
        # Check guess logic...

    def ask_for_input(self):
        # Ask for input logic...

def play_game(word_list):
    """
    Play the Hangman game.

    Parameters:
    - word_list (list): A list of words for the game.
    """
    # Step 1: Create a variable called num_lives and assign it to 5
    num_lives = 5

    # Step 1 (continued): Create an instance of the Hangman class
    game = Hangman(word_list, num_lives)

    # Step 1 (continued): Create a while loop
    while True:
        # Step 1 (continued): Check if num_lives is 0
        if game.num_lives == 0:
            print("You lost!")
            break
        # Step 1 (continued): Check if num_letters is greater than 0
        elif game.num_letters > 0:
            game.ask_for_input()
        # Step 1 (continued): If num_lives is not 0 and num_letters is not greater than 0, user won
        else:
            print("Congratulations. You won the game!")
            break

# Step 2: Call the play_game function
word_list_example = ['apple', 'banana', 'orange', 'grape', 'kiwi']
play_game(word_list_example)