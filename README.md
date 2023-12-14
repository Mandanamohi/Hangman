import random

def generate_random_word(word_list):
    return random.choice(word_list)

def get_user_guess():
    guess = input("Enter a single letter: ")
    return guess

def validate_user_input(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]

    word = generate_random_word(word_list)

    guess = get_user_guess()

    if validate_user_input(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()
