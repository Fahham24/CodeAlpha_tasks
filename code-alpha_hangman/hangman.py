# hangman.py

import random

# 5 predefined words
words = ["python", "computer", "program", "coding", "hangman"]

# Random word select karo
word = random.choice(words)

# Hidden word
guessed_word = ["_"] * len(word)

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

# Guessed letters
guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!\n")


# Result
if "_" not in guessed_word:
    print("Congratulations! You won!")
    print("The word was:", word)
else:
    print("Game Over!")
    print("The correct word was:", word)