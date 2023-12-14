import random
word_list = ["apple", "banana", "kiwi", "strawberry", "mango"]
print (word_list)

word = random.choice(word_list)

print("Randomly generated word:", word)

guess = input("Enter a single letter: ")

print("You entered:", guess)
if len(guess) == 1 and guess.isalpha():

    print("Good guess!")

else:
    print("Oops! That is not a valid input.")
