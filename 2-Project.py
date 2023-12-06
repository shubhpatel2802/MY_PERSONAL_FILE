import random

def hangman():
    words = ["apple", "banana", "cherry", "durian", "elderberry"]  # Add more words to the list if desired
    secret_word = random.choice(words)
    guessed_letters = []
    tries = 6  # Number of tries the player has

    print("Welcome to Hangman!")
    print("_ " * len(secret_word))

    while tries > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter at a time.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        # Display the partially guessed word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Check if the player has won
        if "_" not in display_word:
            print("Congratulations! You won!")
            break

    if tries == 0:
        print("Sorry, you lost. The secret word was:", secret_word)

hangman()