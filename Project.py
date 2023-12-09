import random

# List of secret words
secret_words = ["Apple", "orange", "banana", "mango"]

# Choose a random secret word
secret_word = random.choice(secret_words)

# Initialize variables
guessed_letters = set()
wrong_guesses = 0

# Game loop
while wrong_guesses < 6:
    # Display the current state of the word
    current_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            current_word += letter
        else:
            current_word += "_"

    print(current_word)

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guess is correct
    if guess in secret_word:
        guessed_letters.add(guess)
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Incorrect!")
        print(f"{wrong_guesses} wrong guesses left.")

    # Check if the word has been guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("You win!")
        break

# Game over
if wrong_guesses == 6:
    print("You lose!")
    print(f"The secret word was: {secret_word}")
