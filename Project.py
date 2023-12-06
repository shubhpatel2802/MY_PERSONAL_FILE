import random

def generate_secret_word(words_list):
    secret_word = random.choice(words_list)
    return secret_word

def create_masked_word(secret_word):
    masked_word = '*' * len(secret_word)
    return masked_word

def reveal_letter(secret_word, masked_word, letter):
    secret_word = secret_word.lower()
    letter = letter.lower()

    new_masked_word = ''
    revealed = False

    for char in secret_word:
        if char == letter:
            new_masked_word += letter
            revealed = True
        else:
            new_masked_word += masked_word[secret_word.index(char)]

    return new_masked_word, revealed

def start_game(words_list):
    secret_word = generate_secret_word(words_list)
    masked_word = create_masked_word(secret_word)
    chances = 7
    revealed_letters = ''

    while chances > 0 and masked_word != secret_word:
        print(f'Attempts remaining: {chances}')
        print(f'Masked word: {masked_word}')
        print(f'Revealed letters: {revealed_letters}')

        letter = input('Guess a letter: ').strip()

        if len(letter) != 1 or not letter.isalpha():
            print('Invalid input, please enter a single letter.')
            continue

        if letter in revealed_letters:
            print('You have already guessed that letter.')
            continue

        new_masked_word, revealed = reveal_letter(secret_word, masked_word, letter)

        if revealed:
            revealed_letters += letter
            masked_word = new_masked_word
        else:
            chances -= 1

    if chances == 0:
        print(f'Game over. The secret word was "{secret_word}".')
    else:
        print(f'Congratulations! You have guessed the secret word "{secret_word}".')

if __name__ == '__main__':
    words_list = ['apple', 'banana', 'cherry']
    start_game(words_list)