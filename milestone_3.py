import random

def generate_random_word(word_list):
    return random.choice(word_list)

def main():
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # Step 1: Create an if statement that checks if the guess is in the word.
    secret_word = generate_random_word(word_list)
    guess = input("Enter a single letter: ")

    if guess.isalpha() and len(guess) == 1:
        if guess in secret_word:
            # Step 2: Print a message saying "Good guess! {guess} is in the word."
            print(f"Good guess! {guess} is in the word.")
        else:
            # Step 3: Print a message saying "Sorry, {guess} is not in the word. Try again."
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if __name__ == "__main__":
    main()
